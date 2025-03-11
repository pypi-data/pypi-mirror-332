import dataclasses
from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from dataclasses import field
import json

from zimasabus_sdk.zmsystem import ZmSystem, ZmSystemEnums
from zimasabus_sdk.zimasa.appointments import (
    PagedResponse, 
    TimeSlot, 
    AvailableDate, 
    AvailabilityResponse,
    AppointmentResponse
)


@dataclasses.dataclass
class ProviderUserSearchResponse:
    """
    A class representing the response from the provider user search endpoint.
    
    Attributes:
        id (int): The provider user ID.
        provider (Dict[str, Any]): The provider information.
        member (Dict[str, Any]): The member information.
        role (str): The role of the provider user.
        status (str): The status of the provider user.
        provider_type (str): The type of provider.
    """
    id: int
    provider: Dict[str, Any]
    member: Dict[str, Any]
    role: str
    status: str
    provider_type: str


@dataclasses.dataclass
class AppointmentSearchParameters:
    """
    A class representing the search criteria for retrieving appointments.
    
    Attributes:
        user_entity_id (Optional[str]): The user entity ID.
        provider_service_id (Optional[int]): The provider service ID.
        provider_user_id (Optional[int]): The provider user ID.
        schedule_type_id (Optional[int]): The schedule type ID.
        appointment_date (Optional[str]): The appointment date.
        status (Optional[str]): The appointment status.
        communication_preference (Optional[str]): The communication preference.
        service_mode (Optional[str]): The service mode.
        start_date (Optional[str]): The start date for the search range.
        end_date (Optional[str]): The end date for the search range.
    """
    user_entity_id: Optional[str] = None
    provider_service_id: Optional[int] = None
    provider_user_id: Optional[int] = None
    schedule_type_id: Optional[int] = None
    appointment_date: Optional[str] = None
    status: Optional[str] = None
    communication_preference: Optional[str] = None
    service_mode: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


@dataclasses.dataclass
class AppointmentActionRequest:
    """
    A class representing a request to confirm or cancel an appointment.
    
    Attributes:
        user_entity_id (str): The user entity ID.
        appointment_id (int): The appointment ID.
        action (str): The action to perform (SCHEDULE or CANCEL).
        reason (str): The reason for the action.
    """
    user_entity_id: str
    appointment_id: int
    action: str
    reason: str


@dataclasses.dataclass
class AppointmentRescheduleRequest:
    """
    A class representing a request to reschedule an appointment.
    
    Attributes:
        id (int): The appointment ID.
        notes (str): Notes about the rescheduling.
        appointment_date (str): The new appointment date.
        start_time (str): The new start time.
        duration (int): The duration of the appointment.
        end_time (str): The new end time.
        schedule_type (str): The schedule type.
        communication_preference (str): The communication preference.
        service_mode (str): The service mode.
    """
    id: int
    notes: str
    appointment_date: str
    start_time: str
    duration: int
    end_time: str
    schedule_type: str
    communication_preference: str
    service_mode: str


@dataclasses.dataclass
class FollowUpReport:
    """
    A class representing a follow-up report.
    
    Attributes:
        report_generated (bool): Whether the report was generated.
        report_id (str): The report ID.
        generated_date (str): The date the report was generated.
    """
    report_generated: bool
    report_id: str
    generated_date: str


@dataclasses.dataclass
class FollowUpService:
    """
    A class representing a follow-up service for managing appointment follow-ups.
    
    This service provides methods for retrieving provider user IDs, managing appointments,
    checking available slots, rescheduling appointments, and handling follow-ups.
    
    Attributes:
        system (ZmSystem): The ZmSystem object representing the system.
    """
    system: ZmSystem = dataclasses.field(
        default_factory=lambda: ZmSystem(zm_system_enum=ZmSystemEnums.ZIMASAMED)
    )
    
    def get_provider_user_id(self, user_entity_id: str) -> int:
        """
        Get the provider user ID from the user entity ID.
        
        Args:
            user_entity_id (str): The user entity ID.
            
        Returns:
            int: The provider user ID.
        """
        url = f"{self.system.base_url}zimasa/provider_users/search?userEntityId={user_entity_id}"
        data = self.system.request("get", url)
        
        if isinstance(data, dict) and 'content' in data and data['content']:
            provider_user = data['content'][0]
            return provider_user.get('id')
        
        raise ValueError(f"No provider user found for user entity ID: {user_entity_id}")
    
    def get_appointments(self, search_params: Union[AppointmentSearchParameters, Dict[str, Any]]) -> PagedResponse:
        """
        Fetch appointment details based on search criteria.
        
        Args:
            search_params (Union[AppointmentSearchParameters, Dict[str, Any]]): The search parameters.
            
        Returns:
            PagedResponse: A paged response containing appointment details.
            
        Note:
            The API expects enum values for status, not strings. If you're using the status parameter,
            make sure it matches one of the expected enum values on the server side.
        """
        url = f"{self.system.base_url}zimasa/appointments/search"
        
        # Convert search_params to dictionary if it's an AppointmentSearchParameters object
        if isinstance(search_params, AppointmentSearchParameters):
            params = self._build_search_params(search_params)
        else:
            params = search_params
        
        # Remove status parameter if it's a string to avoid ClassCastException
        if 'status' in params and isinstance(params['status'], str):
            print(f"Warning: Removing status parameter '{params['status']}' to avoid ClassCastException. The API expects an enum value.")
            del params['status']
        
        data = self.system.request("get", url, params=params)
        
        # Convert raw data to AppointmentResponse objects
        appointments = []
        if isinstance(data, dict) and 'content' in data:
            for item in data['content']:
                appointment = self._parse_appointment_response(item)
                appointments.append(appointment)
            
            # Create PagedResponse object
            page_info = data.get('pageInfo', {})
            return PagedResponse(
                content=appointments,
                page_info=page_info
            )
        
        return data  # Return raw data if format is unexpected
    
    def confirm_appointment(self, user_entity_id: str, appointment_id: int, reason: str) -> AppointmentResponse:
        """
        Confirm an existing appointment.
        
        Args:
            user_entity_id (str): The user entity ID.
            appointment_id (int): The appointment ID.
            reason (str): The reason for confirming the appointment.
            
        Returns:
            AppointmentResponse: The updated appointment details.
        """
        url = f"{self.system.base_url}zimasa/appointments/action"
        
        payload = {
            "userEntityId": user_entity_id,
            "appointmentId": appointment_id,
            "action": "SCHEDULE",
            "reason": reason
        }
        
        data = self.system.request("put", url, json=payload)
        return self._parse_appointment_response(data)
    
    def reject_appointment(self, user_entity_id: str, appointment_id: int, reason: str) -> AppointmentResponse:
        """
        Reject/cancel an existing appointment.
        
        Args:
            user_entity_id (str): The user entity ID.
            appointment_id (int): The appointment ID.
            reason (str): The reason for rejecting the appointment.
            
        Returns:
            AppointmentResponse: The updated appointment details.
        """
        url = f"{self.system.base_url}zimasa/appointments/action"
        
        payload = {
            "userEntityId": user_entity_id,
            "appointmentId": appointment_id,
            "action": "CANCEL",
            "reason": reason
        }
        
        data = self.system.request("put", url, json=payload)
        return self._parse_appointment_response(data)
    
    def get_available_slots(self, provider_service_id: int, year: int, month: int) -> AvailabilityResponse:
        """
        Get available appointment slots for a provider service.
        
        Args:
            provider_service_id (int): The provider service ID.
            year (int): The year to check availability for.
            month (int): The month to check availability for.
            
        Returns:
            AvailabilityResponse: The available dates and time slots.
        """
        url = f"{self.system.base_url}zimasa/appointments/available-slots"
        
        params = {
            "providerServiceId": provider_service_id,
            "year": year,
            "month": month
        }
        
        data = self.system.request("get", url, params=params)
        
        # Parse the response into AvailabilityResponse
        available_dates = []
        if isinstance(data, dict) and 'availableDates' in data:
            for date_data in data['availableDates']:
                time_slots = []
                for slot_data in date_data.get('timeSlots', []):
                    time_slot = TimeSlot(
                        start_time=slot_data.get('startTime'),
                        end_time=slot_data.get('endTime'),
                        booked=slot_data.get('booked', False)
                    )
                    time_slots.append(time_slot)
                
                available_date = AvailableDate(
                    date=date_data.get('date'),
                    time_slots=time_slots
                )
                available_dates.append(available_date)
            
            return AvailabilityResponse(
                available_dates=available_dates
            )
        
        return data  # Return raw data if format is unexpected
    
    def reschedule_appointment(self, reschedule_request: Union[AppointmentRescheduleRequest, Dict[str, Any]]) -> AppointmentResponse:
        """
        Reschedule an existing appointment.
        
        Args:
            reschedule_request (Union[AppointmentRescheduleRequest, Dict[str, Any]]): The reschedule request.
            
        Returns:
            AppointmentResponse: The updated appointment details.
        """
        url = f"{self.system.base_url}zimasa/appointments/reschedule"
        
        # Convert reschedule_request to dictionary if it's an AppointmentRescheduleRequest object
        if isinstance(reschedule_request, AppointmentRescheduleRequest):
            payload = self._build_reschedule_request(
                reschedule_request.id,
                reschedule_request.appointment_date,
                reschedule_request.start_time,
                reschedule_request.end_time,
                reschedule_request.notes,
                reschedule_request.schedule_type,
                reschedule_request.communication_preference,
                reschedule_request.service_mode
            )
        else:
            payload = reschedule_request
        
        data = self.system.request("put", url, json=payload)
        return self._parse_appointment_response(data)
    
    def extract_appointment_details(self, appointment: AppointmentResponse) -> Dict[str, Any]:
        """
        Analyze appointment information to determine follow-up requirements.
        
        Args:
            appointment (AppointmentResponse): The appointment object.
            
        Returns:
            Dict[str, Any]: Structured data about follow-up requirements.
        """
        # Extract relevant details from the appointment
        follow_up_data = {
            "appointment_id": appointment.id,
            "patient_name": f"{appointment.member.first_name} {appointment.member.last_name}" if appointment.member else "Unknown",
            "appointment_date": appointment.appointment_date,
            "appointment_time": appointment.start_time,
            "service_name": appointment.service.name if appointment.service else "Unknown",
            "needs_followup": self._determine_if_needs_followup(appointment),
            "recommended_followup_date": self._calculate_followup_date(appointment),
            "notes": appointment.notes
        }
        
        return follow_up_data
    
    def schedule_followup(self, original_appointment_id: int, follow_up_date: str, follow_up_time: str, notes: str) -> AppointmentResponse:
        """
        Create a follow-up appointment based on an original appointment.
        
        Args:
            original_appointment_id (int): The original appointment ID.
            follow_up_date (str): The date for the follow-up.
            follow_up_time (str): The time for the follow-up.
            notes (str): Notes for the follow-up appointment.
            
        Returns:
            AppointmentResponse: The new appointment details.
        """
        # First, get the original appointment details
        url = f"{self.system.base_url}zimasa/appointments/{original_appointment_id}"
        original_appointment_data = self.system.request("get", url)
        original_appointment = self._parse_appointment_response(original_appointment_data)
        
        # Calculate end time (assuming 30-minute duration)
        start_time_parts = follow_up_time.split(':')
        hour = int(start_time_parts[0])
        minute = int(start_time_parts[1])
        
        # Add 30 minutes
        minute += 30
        if minute >= 60:
            hour += 1
            minute -= 60
        
        end_time = f"{hour:02d}:{minute:02d}:00"
        
        # Create a new appointment with the follow-up details
        create_url = f"{self.system.base_url}zimasa/appointments"
        
        payload = {
            "notes": f"Follow-up for appointment #{original_appointment_id}. {notes}",
            "appointmentDate": follow_up_date,
            "startTime": follow_up_time,
            "endTime": end_time,
            "scheduleType": original_appointment.schedule_type.id if original_appointment.schedule_type else 1,
            "communicationPreference": "SMS",
            "serviceMode": "IN_PERSON",
            "providerServiceId": original_appointment.service.id if original_appointment.service else None,
            "userEntityId": original_appointment.member.id if original_appointment.member else None
        }
        
        data = self.system.request("post", create_url, json=payload)
        return self._parse_appointment_response(data)
    
    def send_followup_notification(self, appointment_id: int, notification_type: str, message: str) -> Dict[str, Any]:
        """
        Send notifications about follow-ups.
        
        Args:
            appointment_id (int): The appointment ID.
            notification_type (str): The type of notification (SMS, EMAIL, etc.).
            message (str): The notification message.
            
        Returns:
            Dict[str, Any]: Notification status.
        """
        url = f"{self.system.base_url}zimasa/notifications"
        
        payload = {
            "appointmentId": appointment_id,
            "type": notification_type,
            "message": message
        }
        
        data = self.system.request("post", url, json=payload)
        return data
    
    def conduct_followup(self, appointment_id: int, follow_up_method: str, notes: str) -> Dict[str, Any]:
        """
        Record that a follow-up was conducted.
        
        Args:
            appointment_id (int): The appointment ID.
            follow_up_method (str): The method used for the follow-up.
            notes (str): Notes about the follow-up.
            
        Returns:
            Dict[str, Any]: Follow-up status.
        """
        url = f"{self.system.base_url}zimasa/appointments/{appointment_id}/followup"
        
        payload = {
            "method": follow_up_method,
            "notes": notes,
            "conductedAt": datetime.now().isoformat()
        }
        
        data = self.system.request("post", url, json=payload)
        return data
    
    def generate_followup_report(self, criteria: Dict[str, Any]) -> FollowUpReport:
        """
        Create reports about follow-ups.
        
        Args:
            criteria (Dict[str, Any]): Report criteria (date range, provider, etc.).
            
        Returns:
            FollowUpReport: Report data.
            
        Note:
            This method attempts to use the /zimasa/reports/followups endpoint, which may not exist.
            In a production environment, you should confirm the correct endpoint for generating reports.
        """
        # Try the reports endpoint first
        url = f"{self.system.base_url}zimasa/reports/followups"
        
        try:
            data = self.system.request("post", url, json=criteria)
            
            if isinstance(data, dict):
                return FollowUpReport(
                    report_generated=data.get('reportGenerated', False),
                    report_id=data.get('reportID', ''),
                    generated_date=data.get('generatedDate', '')
                )
        except Exception as e:
            print(f"Warning: Error accessing reports endpoint: {e}")
            print("Trying alternative endpoint...")
            
            # Try an alternative endpoint
            try:
                alt_url = f"{self.system.base_url}zimasa/appointments/reports"
                data = self.system.request("post", alt_url, json=criteria)
                
                if isinstance(data, dict):
                    return FollowUpReport(
                        report_generated=data.get('reportGenerated', True),
                        report_id=data.get('reportID', 'generated-report'),
                        generated_date=datetime.now().isoformat()
                    )
            except Exception as alt_e:
                print(f"Warning: Error accessing alternative reports endpoint: {alt_e}")
                # Fall through to return a default report
        
        # If all attempts fail, return a default report
        print("Warning: Could not generate report. Returning default report.")
        return FollowUpReport(
            report_generated=False,
            report_id='',
            generated_date=''
        )
    
    # Helper methods
    
    def _build_search_params(self, search_params: AppointmentSearchParameters) -> Dict[str, Any]:
        """
        Convert Python parameters to API-compatible format.
        
        Args:
            search_params (AppointmentSearchParameters): The search parameters.
            
        Returns:
            Dict[str, Any]: Formatted search parameters dictionary.
        """
        params = {}
        
        if search_params.user_entity_id:
            params['userEntityId'] = search_params.user_entity_id
        
        if search_params.provider_service_id:
            params['providerServiceId'] = search_params.provider_service_id
        
        if search_params.provider_user_id:
            params['providerUserId'] = search_params.provider_user_id
        
        if search_params.schedule_type_id:
            params['scheduleTypeId'] = search_params.schedule_type_id
        
        if search_params.appointment_date:
            params['appointmentDate'] = search_params.appointment_date
        
        if search_params.status:
            params['status'] = search_params.status
        
        if search_params.communication_preference:
            params['communicationPreference'] = search_params.communication_preference
        
        if search_params.service_mode:
            params['serviceMode'] = search_params.service_mode
        
        if search_params.start_date:
            params['startDate'] = search_params.start_date
        
        if search_params.end_date:
            params['endDate'] = search_params.end_date
        
        return params
    
    def _parse_appointment_response(self, data: Dict[str, Any]) -> AppointmentResponse:
        """
        Convert API response to Python objects.
        
        Args:
            data (Dict[str, Any]): API response data.
            
        Returns:
            AppointmentResponse: Structured appointment data.
        """
        # Instead of relying on AppointmentService, implement the parsing directly
        try:
            from zimasabus_sdk.zimasa.appointments import (
                AppointmentResponse, 
                AppointmentMember, 
                AppointmentScheduleType,
                ProviderService
            )
            
            # Parse member data
            member_data = data.get('member', {})
            member = None
            if member_data:
                member = AppointmentMember(
                    id=member_data.get('id', ''),
                    email=member_data.get('email'),
                    email_verified=member_data.get('emailVerified'),
                    enabled=member_data.get('enabled'),
                    first_name=member_data.get('firstName'),
                    last_name=member_data.get('lastName'),
                    username=member_data.get('username'),
                    phone=member_data.get('phone'),
                    address=member_data.get('address'),
                    date_of_birth=member_data.get('dateOfBirth'),
                    created_at=member_data.get('createdAt'),
                    updated_at=member_data.get('updatedAt')
                )
            
            # Parse schedule type data
            schedule_type_data = data.get('scheduleType', {})
            schedule_type = None
            if schedule_type_data:
                schedule_type = AppointmentScheduleType(
                    id=schedule_type_data.get('id', 0),
                    name=schedule_type_data.get('name'),
                    description=schedule_type_data.get('description'),
                    slot_duration_minutes=schedule_type_data.get('slotDurationMinutes'),
                    break_duration_minutes=schedule_type_data.get('breakDurationMinutes')
                )
            
            # Parse service data
            service_data = data.get('service', {})
            service = None
            if service_data:
                service = ProviderService(
                    id=service_data.get('id', 0),
                    name=service_data.get('name'),
                    description=service_data.get('description'),
                    duration=service_data.get('duration'),
                    price=service_data.get('price'),
                    is_active=service_data.get('isActive'),
                    service_category=None,  # Simplified for now
                    maximum_capacity=service_data.get('maximumCapacity'),
                    duration_mins=service_data.get('durationMins'),
                    availability=service_data.get('availability'),
                    start_date=service_data.get('startDate'),
                    end_date=service_data.get('endDate'),
                    insurance_accepted=service_data.get('insuranceAccepted'),
                    tags=service_data.get('tags'),
                    service_mode=service_data.get('serviceMode'),
                    service_location=service_data.get('serviceLocation'),
                    created_at=service_data.get('createdAt'),
                    updated_at=service_data.get('updatedAt'),
                    provider_user=None,  # Simplified for now
                    provider_service_payment_methods=None,  # Simplified for now
                    service_handlers=None,  # Simplified for now
                    service_availability=None  # Simplified for now
                )
            
            # Create and return the AppointmentResponse
            return AppointmentResponse(
                id=data.get('id', 0),
                start_time=data.get('startTime', ''),
                end_time=data.get('endTime', ''),
                appointment_date=data.get('appointmentDate', ''),
                notes=data.get('notes'),
                status=data.get('status', ''),
                action_reason=data.get('actionReason'),
                member=member,
                service=service,
                schedule_type=schedule_type,
                created_at=data.get('createdAt'),
                updated_at=data.get('updatedAt')
            )
        except Exception as e:
            print(f"Error parsing appointment response: {e}")
            # Return a simplified AppointmentResponse with just the essential fields
            from zimasabus_sdk.zimasa.appointments import AppointmentResponse
            return AppointmentResponse(
                id=data.get('id', 0),
                start_time=data.get('startTime', ''),
                end_time=data.get('endTime', ''),
                appointment_date=data.get('appointmentDate', ''),
                notes=data.get('notes'),
                status=data.get('status', ''),
                action_reason=data.get('actionReason'),
                member=None,
                service=None,
                schedule_type=None,
                created_at=data.get('createdAt'),
                updated_at=data.get('updatedAt')
            )
    
    def _format_date_time(self, date: str, time: str) -> str:
        """
        Ensure dates and times are in the correct format.
        
        Args:
            date (str): The date string.
            time (str): The time string.
            
        Returns:
            str: Formatted date/time string.
        """
        # Format the date and time according to the API requirements
        return f"{date}T{time}.000Z"
    
    def _extract_user_id_from_token(self, token: str) -> str:
        """
        Extract the user ID from a JWT token.
        
        Args:
            token (str): JWT token.
            
        Returns:
            str: User ID string.
        """
        # In a real implementation, this would decode the JWT token and extract the user ID
        # For simplicity, we'll just return a placeholder
        return "user_id_from_token"
    
    def _build_reschedule_request(self, appointment_id: int, appointment_date: str, start_time: str, end_time: str, notes: str, schedule_type: str, communication_preference: str, service_mode: str) -> Dict[str, Any]:
        """
        Build a request payload for rescheduling an appointment.
        
        Args:
            appointment_id (int): The appointment ID.
            appointment_date (str): The new appointment date.
            start_time (str): The new start time.
            end_time (str): The new end time.
            notes (str): Notes about the rescheduling.
            schedule_type (str): The schedule type.
            communication_preference (str): The communication preference.
            service_mode (str): The service mode.
            
        Returns:
            Dict[str, Any]: Formatted request payload.
        """
        return {
            "id": appointment_id,
            "notes": notes,
            "appointmentDate": appointment_date,
            "startTime": start_time,
            "endTime": end_time,
            "scheduleType": schedule_type,
            "communicationPreference": communication_preference,
            "serviceMode": service_mode
        }
    
    def _determine_if_needs_followup(self, appointment: AppointmentResponse) -> bool:
        """
        Determine if an appointment needs a follow-up.
        
        Args:
            appointment (AppointmentResponse): The appointment object.
            
        Returns:
            bool: Whether the appointment needs a follow-up.
        """
        # This is a placeholder implementation
        # In a real implementation, this would analyze the appointment details
        # to determine if a follow-up is needed
        return True
    
    def _calculate_followup_date(self, appointment: AppointmentResponse) -> str:
        """
        Calculate the recommended follow-up date.
        
        Args:
            appointment (AppointmentResponse): The appointment object.
            
        Returns:
            str: The recommended follow-up date.
        """
        # This is a placeholder implementation
        # In a real implementation, this would calculate a recommended follow-up date
        # based on the appointment details
        
        # For simplicity, we'll just add 30 days to the appointment date
        from datetime import datetime, timedelta
        
        if appointment.appointment_date:
            try:
                # Parse the appointment date
                appointment_date = datetime.strptime(appointment.appointment_date.split('T')[0], "%Y-%m-%d")
                
                # Add 30 days
                followup_date = appointment_date + timedelta(days=30)
                
                # Format the date
                return followup_date.strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Error calculating follow-up date: {e}")
        
        return "" 