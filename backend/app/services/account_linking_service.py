from backend.app.utilities.encryption import encrypt_data
from backend.app.utilities.validation import validate_email
from backend.app.models.account import Account
from backend.app.logger import logger

class AccountLinkingService:
    def link_accounts(self, primary_account_id: int, secondary_account_email: str) -> bool:
        '''
        Links two accounts based on primary account ID and secondary account email.
        Returns True if linking is successful, False otherwise.
        '''
        try:
            # Validate email
            if not validate_email(secondary_account_email):
                logger.error("Invalid email provided for account linking: {}", secondary_account_email)
                return False

            # Fetch accounts
            primary_account = Account.get_by_id(primary_account_id)
            secondary_account = Account.get_by_email(secondary_account_email)

            if not primary_account or not secondary_account:
                logger.error("Account not found for linking. Primary ID: {}, Secondary Email: {}",
                             primary_account_id, secondary_account_email)
                return False

            # Encrypt and store the linking info
            link_info = encrypt_data(f"{primary_account_id}-{secondary_account.id}")
            primary_account.linked_accounts.append(link_info)
            primary_account.save()

            logger.info("Accounts linked successfully. Primary ID: {}, Secondary ID: {}",
                        primary_account_id, secondary_account.id)
            return True

        except Exception as e:
            logger.exception("Failed to link accounts: {}", str(e))
            return False
