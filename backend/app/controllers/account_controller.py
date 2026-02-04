from fastapi import APIRouter, HTTPException, Depends
from backend.app.services.account_linking_service import AccountLinkingService
from backend.app.models.account import Account
from backend.app.auth import get_current_user

router = APIRouter()

@router.post("/accounts/link")
async def link_account(secondary_account_email: str, current_user: Account = Depends(get_current_user)):
    '''
    Endpoint to link the current user's account with another account via email.
    '''
    account_linking_service = AccountLinkingService()
    if account_linking_service.link_accounts(current_user.id, secondary_account_email):
        return {"message": "Account linked successfully."}
    else:
        raise HTTPException(status_code=400, detail="Failed to link accounts.")
