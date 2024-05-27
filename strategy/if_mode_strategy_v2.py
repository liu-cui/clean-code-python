def admin_action(x):
    return f"Performing admin task {x}"

def user_action(x):
    return "Executing standard user operations."

def guest_action(x):
    return "Display guest content."


role_actions = {
    "admin": admin_action,
    "user": user_action,
    "guest": guest_action
}


def perform_action(role, x):
    action_func = role_actions.get(role, lambda: "Invalid role.")
    return action_func(x)


print(perform_action("admin", 1))