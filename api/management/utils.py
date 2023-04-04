from api.models import User


def check_user(user_id: str):
    # Find the user from table
    user = None
    try:
        user = User.objects.all().filter(user_id=user_id).last()
    except:
        pass

    # Failed to find user, or password error
    return user
