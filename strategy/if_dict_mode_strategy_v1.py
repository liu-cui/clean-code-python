"""
设想一个应用场景: 在一个复杂的系统中, 不同用户角色拥有不同的权限, 直接使用if-elif-else来判断角色并分配权限既繁琐又不易扩展.
假设每个角色还可以操作相同的一些事情, 则函数入参数也可作些文.

权限字典直接返回处理函数: 通过将角色与对应的操作函数映射到字典中，我们可以直接根据角色名调用相应的函数
"""

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