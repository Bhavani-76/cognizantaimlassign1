class AppointmentNotFoundException(Exception):
    """Exception raised when an appointment is not found."""
    
    def __init__(self, message="Appointment not found"):
        self.message = message
        super().__init__(self.message)
    
