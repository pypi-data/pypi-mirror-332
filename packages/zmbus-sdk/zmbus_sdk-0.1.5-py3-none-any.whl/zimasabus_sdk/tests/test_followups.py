"""
Tests for the FollowUpService class.
"""

import unittest
from unittest.mock import patch, MagicMock

from zimasabus_sdk.zimasa.followups import (
    FollowUpService,
    AppointmentSearchParameters,
    AppointmentRescheduleRequest,
    FollowUpReport
)


class TestFollowUpService(unittest.TestCase):
    """Test cases for the FollowUpService class."""

    def setUp(self):
        """Set up test fixtures."""
        self.service = FollowUpService()
        # Mock the system object
        self.service.system = MagicMock()
        self.service.system.base_url = "http://test-api.com/"

    def test_get_provider_user_id(self):
        """Test getting a provider user ID."""
        # Mock the response
        mock_response = {
            "content": [
                {
                    "id": 123,
                    "provider": {"name": "Test Provider"},
                    "member": {"firstName": "John", "lastName": "Doe"},
                    "role": "DOCTOR",
                    "status": "ACTIVE",
                    "providerType": "SPECIALIST"
                }
            ]
        }
        self.service.system.request.return_value = mock_response

        # Call the method
        result = self.service.get_provider_user_id("test-user-id")

        # Verify the result
        self.assertEqual(result, 123)
        self.service.system.request.assert_called_once_with(
            "get", 
            "http://test-api.com/zimasa/provider_users/search?userEntityId=test-user-id"
        )

    def test_get_appointments(self):
        """Test getting appointments."""
        # Mock the response
        mock_response = {
            "content": [
                {
                    "id": 456,
                    "startTime": "09:00:00",
                    "endTime": "10:00:00",
                    "appointmentDate": "2025-03-15T09:00:00.000Z",
                    "notes": "Test appointment",
                    "status": "SCHEDULED"
                }
            ],
            "pageInfo": {
                "pageNumber": 1,
                "pageSize": 10,
                "totalElements": 1,
                "totalPages": 1,
                "isFirst": True,
                "isLast": True,
                "isEmpty": False
            }
        }
        self.service.system.request.return_value = mock_response

        # Mock the _parse_appointment_response method
        mock_appointment = MagicMock()
        self.service._parse_appointment_response = MagicMock(return_value=mock_appointment)

        # Call the method
        search_params = AppointmentSearchParameters(provider_user_id=123)
        result = self.service.get_appointments(search_params)

        # Verify the result
        self.assertEqual(len(result.content), 1)
        self.assertEqual(result.content[0], mock_appointment)
        self.service.system.request.assert_called_once_with(
            "get", 
            "http://test-api.com/zimasa/appointments/search",
            params={"providerUserId": 123}
        )

    def test_confirm_appointment(self):
        """Test confirming an appointment."""
        # Mock the response
        mock_response = {
            "id": 456,
            "status": "SCHEDULED"
        }
        self.service.system.request.return_value = mock_response

        # Mock the _parse_appointment_response method
        mock_appointment = MagicMock()
        self.service._parse_appointment_response = MagicMock(return_value=mock_appointment)

        # Call the method
        result = self.service.confirm_appointment("test-user-id", 456, "Slot time available")

        # Verify the result
        self.assertEqual(result, mock_appointment)
        self.service.system.request.assert_called_once_with(
            "put", 
            "http://test-api.com/zimasa/appointments/action",
            json={
                "userEntityId": "test-user-id",
                "appointmentId": 456,
                "action": "SCHEDULE",
                "reason": "Slot time available"
            }
        )

    def test_reject_appointment(self):
        """Test rejecting an appointment."""
        # Mock the response
        mock_response = {
            "id": 456,
            "status": "CANCELLED"
        }
        self.service.system.request.return_value = mock_response

        # Mock the _parse_appointment_response method
        mock_appointment = MagicMock()
        self.service._parse_appointment_response = MagicMock(return_value=mock_appointment)

        # Call the method
        result = self.service.reject_appointment("test-user-id", 456, "Patient request")

        # Verify the result
        self.assertEqual(result, mock_appointment)
        self.service.system.request.assert_called_once_with(
            "put", 
            "http://test-api.com/zimasa/appointments/action",
            json={
                "userEntityId": "test-user-id",
                "appointmentId": 456,
                "action": "CANCEL",
                "reason": "Patient request"
            }
        )

    def test_get_available_slots(self):
        """Test getting available slots."""
        # Mock the response
        mock_response = {
            "availableDates": [
                {
                    "date": "2025-03-15",
                    "timeSlots": [
                        {
                            "startTime": "09:00:00",
                            "endTime": "09:30:00",
                            "booked": False
                        },
                        {
                            "startTime": "09:30:00",
                            "endTime": "10:00:00",
                            "booked": True
                        }
                    ]
                }
            ]
        }
        self.service.system.request.return_value = mock_response

        # Call the method
        result = self.service.get_available_slots(70, 2025, 3)

        # Verify the result
        self.assertEqual(len(result.available_dates), 1)
        self.assertEqual(result.available_dates[0].date, "2025-03-15")
        self.assertEqual(len(result.available_dates[0].time_slots), 2)
        self.assertEqual(result.available_dates[0].time_slots[0].start_time, "09:00:00")
        self.assertEqual(result.available_dates[0].time_slots[0].end_time, "09:30:00")
        self.assertEqual(result.available_dates[0].time_slots[0].booked, False)
        self.service.system.request.assert_called_once_with(
            "get", 
            "http://test-api.com/zimasa/appointments/available-slots",
            params={
                "providerServiceId": 70,
                "year": 2025,
                "month": 3
            }
        )

    def test_reschedule_appointment(self):
        """Test rescheduling an appointment."""
        # Mock the response
        mock_response = {
            "id": 456,
            "appointmentDate": "2025-03-20T09:00:00.000Z",
            "status": "SCHEDULED"
        }
        self.service.system.request.return_value = mock_response

        # Mock the _parse_appointment_response method
        mock_appointment = MagicMock()
        self.service._parse_appointment_response = MagicMock(return_value=mock_appointment)

        # Call the method
        reschedule_request = AppointmentRescheduleRequest(
            id=456,
            notes="Appointment Rescheduled",
            appointment_date="2025-03-20T09:00:00.000Z",
            start_time="09:00:00",
            duration=30,
            end_time="09:30:00",
            schedule_type="3",
            communication_preference="SMS",
            service_mode="IN_PERSON"
        )
        result = self.service.reschedule_appointment(reschedule_request)

        # Verify the result
        self.assertEqual(result, mock_appointment)
        self.service.system.request.assert_called_once_with(
            "put", 
            "http://test-api.com/zimasa/appointments/reschedule",
            json={
                "id": 456,
                "notes": "Appointment Rescheduled",
                "appointmentDate": "2025-03-20T09:00:00.000Z",
                "startTime": "09:00:00",
                "endTime": "09:30:00",
                "scheduleType": "3",
                "communicationPreference": "SMS",
                "serviceMode": "IN_PERSON"
            }
        )

    def test_generate_followup_report(self):
        """Test generating a follow-up report."""
        # Mock the response
        mock_response = {
            "reportGenerated": True,
            "reportID": "report-123",
            "generatedDate": "2025-03-15T10:00:00.000Z"
        }
        self.service.system.request.return_value = mock_response

        # Call the method
        criteria = {
            "startDate": "2025-01-01",
            "endDate": "2025-12-31",
            "providerUserId": 123
        }
        result = self.service.generate_followup_report(criteria)

        # Verify the result
        self.assertIsInstance(result, FollowUpReport)
        self.assertEqual(result.report_generated, True)
        self.assertEqual(result.report_id, "report-123")
        self.assertEqual(result.generated_date, "2025-03-15T10:00:00.000Z")
        self.service.system.request.assert_called_once_with(
            "post", 
            "http://test-api.com/zimasa/reports/followups",
            json=criteria
        )


if __name__ == "__main__":
    unittest.main() 