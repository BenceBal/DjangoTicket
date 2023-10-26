from django.test import TestCase
import unittest
from .models import SeasonTicket, MyTicket, Match


# Create your tests here.
class TestTickets(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def setUp(self):        
        self.match = Match.objects.create(season="Test Season", matchName="Test Match")

    def test_new_ticket_saved(self):
        ticket = MyTicket.objects.create(Ticketid="testtick1", price=20.00, matchEvent=self.match)
        queried_ticket = MyTicket.objects.filter(Ticketid="testtick1").first()
        self.assertIsNotNone(queried_ticket)

        def test_ticket_match_event(self):
            # Test if the Ticket is associated with the correct Match object
            self.assertEqual(self.ticket.matchEvent.matchName, "Test Match")
    
    # Delete the test match from the database
    # self.match.delete()
    # ticket.delete()

class TestMatchEntity(TestCase):
    def CreatePersistReloadMatch(self):
        # Create a new Match entity
        new_match = Match.objects.create(
            season="Summer",
            matchName="Test2 Match",
            capacity=50,
            capacityFanSector=20
        )

        # Retrieve the match from the database
        retrieved_match = Match.objects.get(id=new_match.id)

        # Check the attributes of the retrieved match
        self.assertEqual(retrieved_match.season, "Summer")
        self.assertEqual(retrieved_match.matchName, "Test2 Match")
        self.assertEqual(retrieved_match.capacity, 50)
        self.assertEqual(retrieved_match.capacityFanSector, 20)

        # Check auto-generated eventTime field (within a reasonable time difference)
        time_difference = retrieved_match.eventTime - new_match.eventTime
        self.assertLessEqual(time_difference.seconds, 10)  # Allow a 10-second difference for auto_now_add field

        # Optionally, you can add more assertions based on your specific requirements
        # For example, check if retrieved_match.id exists, or check for other field values.

        # Delete the test match from the database
        # retrieved_match.delete()

        # Verify the match is deleted
        # self.assertIsNotNone(new_match)
        self.assertIsNotNone(new_match)

    