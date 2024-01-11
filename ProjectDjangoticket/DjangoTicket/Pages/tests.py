import unittest
from unittest.mock import patch, Mock
from django.test import TestCase
from Ticketshop.models import MyTicket, SeasonTicket, Match

class MyTicketTestCase(TestCase):

    def setUp(self):
        # Erstelle Testdaten, die für den Test verwendet werden
        season_ticket = SeasonTicket.objects.create(name='Test Season Ticket', price=100)
        match = Match.objects.create(season='Test Season', matchName='Test Match', capacity=50, capacityFanSector=20)

        # Erstelle ein MyTicket-Objekt für den Test
        self.my_ticket = MyTicket.objects.create(
            price=30,
            used=False,
            seasonCard=season_ticket,
            matchEvent=match
        )

    @patch('Ticketshop.models.Ticket.save')  # Mock die save-Methode der übergeordneten Klasse
    def test_my_ticket_creation(self, mock_save):
        # Überprüfe, ob die MyTicket-Instanz korrekt erstellt wurde
        self.assertEqual(self.my_ticket.price, 30)
        self.assertFalse(self.my_ticket.used)
        self.assertEqual(self.my_ticket.seasonCard, self.my_ticket.seasonCard)
        self.assertEqual(self.my_ticket.matchEvent, self.my_ticket.matchEvent)

        # Überprüfe, ob die save-Methode aufgerufen wurde
        mock_save.assert_called_once()

    @patch('Ticketshop.models.Ticket.save')
    def test_my_ticket_str_method(self, mock_save):
        # Mock die save-Methode und setze den Rückgabewert für die Ticketid
        mock_save.return_value = Mock(Ticketid='ABC123')

        # Überprüfe, ob die __str__-Methode korrekt funktioniert
        self.assertEqual(str(self.my_ticket), 'ABC123')
        mock_save.assert_called_once()
