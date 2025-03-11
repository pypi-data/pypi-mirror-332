"""
Example script demonstrating how to use the FollowUpService class.
"""

from zimasabus_sdk.zimasa import FollowUpService
from zimasabus_sdk.zimasa.followups import AppointmentSearchParameters, AppointmentRescheduleRequest

def main():
    # Initialize the service
    followup_service = FollowUpService()
    
    try:
        # Example 1: Get provider user ID
        print("Example 1: Get provider user ID")
        provider_id = followup_service.get_provider_user_id("f11f84b1-0368-417f-8be3-cad503a916ed")
        print(f"Provider ID: {provider_id}")
        print()
        
        # Example 2: Get appointments for the provider
        print("Example 2: Get appointments for the provider")
        search_params = AppointmentSearchParameters(
            provider_user_id=provider_id
        )
        appointments = followup_service.get_appointments(search_params)
        print(f"Found {len(appointments.content)} appointments")
        
        # Print the first appointment if available
        if appointments.content:
            appointment = appointments.content[0]
            print(f"First appointment: ID={appointment.id}, Date={appointment.appointment_date}, Status={appointment.status}")
        print()
        
        # Example 3: Check available slots for rescheduling
        print("Example 3: Check available slots for rescheduling")
        available_slots = followup_service.get_available_slots(70, 2025, 3)
        print(f"Available dates: {len(available_slots.available_dates)}")
        
        # Print the first available date if available
        if available_slots.available_dates:
            date = available_slots.available_dates[0]
            print(f"First available date: {date.date}, Slots: {len(date.time_slots)}")
        print()
        
        # Example 4: Extract appointment details for follow-up
        print("Example 4: Extract appointment details for follow-up")
        if appointments.content:
            appointment = appointments.content[0]
            follow_up_data = followup_service.extract_appointment_details(appointment)
            print(f"Follow-up data: {follow_up_data}")
            print(f"Needs follow-up: {follow_up_data['needs_followup']}")
            print(f"Recommended follow-up date: {follow_up_data['recommended_followup_date']}")
        print()
        
        # Example 5: Schedule a follow-up appointment
        print("Example 5: Schedule a follow-up appointment")
        if appointments.content:
            appointment = appointments.content[0]
            follow_up_date = "2025-04-15"
            follow_up_time = "10:00:00"
            notes = "Regular follow-up appointment"
            
            try:
                follow_up_appointment = followup_service.schedule_followup(
                    appointment.id,
                    follow_up_date,
                    follow_up_time,
                    notes
                )
                print(f"Follow-up appointment scheduled: ID={follow_up_appointment.id}")
            except Exception as e:
                print(f"Error scheduling follow-up: {e}")
        print()
        
        # Example 6: Generate a follow-up report
        print("Example 6: Generate a follow-up report")
        criteria = {
            "startDate": "2025-01-01",
            "endDate": "2025-12-31",
            "providerUserId": provider_id
        }
        
        report = followup_service.generate_followup_report(criteria)
        print(f"Report generated: {report.report_generated}")
        if report.report_generated:
            print(f"Report ID: {report.report_id}")
            print(f"Generated date: {report.generated_date}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 