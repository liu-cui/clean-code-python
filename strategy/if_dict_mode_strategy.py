"""
设想一个应用场景: 在一个复杂的系统中, 不同用户角色拥有不同的权限, 直接使用if-elif-else来判断角色并分配权限既繁琐又不易扩展.

权限字典直接返回处理函数: 通过将角色与对应的操作函数映射到字典中，我们可以直接根据角色名调用相应的函数
"""


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