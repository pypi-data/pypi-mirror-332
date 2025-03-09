class DNAWaveError(Exception):
    """Base exception for DNAWave API errors"""
    pass

class AuthenticationError(DNAWaveError):
    """Authentication related errors"""
    pass

class ValidationError(DNAWaveError):
    """Validation related errors"""
    pass
