from vk_api.keyboard import VkKeyboard, VkKeyboardColor



keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Hello', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Goodbay', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=222723275")


test_keyboard = VkKeyboard(one_time=True, inline=True)
test_keyboard.add_button('A')
test_keyboard.add_button('B')
test_keyboard.add_button('C')
test_keyboard.add_button('D')

