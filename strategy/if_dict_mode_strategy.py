def admin_action():
    return "Performing admin task"

def user_action():
    return "Executing standard user operations."

def guest_action():
    return "Display guest content."


role_actions = {
    "admin": admin_action,
    "user": user_action,
    "guest": guest_action
}


def perform_action(role):
    action_func = role_actions.get(role, lambda: "Invalid role.")
    return action_func()


print(perform_action("admin"))