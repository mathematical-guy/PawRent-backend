from account_management.constants import UserConstants

USER_TYPES_CHOICES = (
    (UserConstants.UserType.ADMIN, "Admin"),
    (UserConstants.UserType.OWNER, "Owner"),
    (UserConstants.UserType.RENTER, "Renter"),
)