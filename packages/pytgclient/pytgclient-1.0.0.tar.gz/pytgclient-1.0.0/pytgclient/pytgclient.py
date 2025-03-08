import requests

class Client:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, chat_id, text, parse_mode="HTML"):
        """ إرسال رسالة نصية عادية """
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
        return requests.post(url, json=payload).json()

    def send_message_with_inline_button(self, chat_id, text, buttons):
        """ إرسال رسالة تحتوي على أزرار إنلاين """
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": chat_id, "text": text, "reply_markup": {"inline_keyboard": buttons}, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def edit_message_text(self, chat_id, message_id, new_text):
        """ تعديل نص رسالة قديمة """
        url = f"{self.base_url}/editMessageText"
        payload = {"chat_id": chat_id, "message_id": message_id, "text": new_text, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def edit_message_reply_markup(self, chat_id, message_id, buttons):
        """ تعديل الأزرار في رسالة قديمة """
        url = f"{self.base_url}/editMessageReplyMarkup"
        payload = {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": buttons}}
        return requests.post(url, json=payload).json()

    def delete_message(self, chat_id, message_id):
        """ حذف رسالة من القناة أو الدردشة """
        url = f"{self.base_url}/deleteMessage"
        payload = {"chat_id": chat_id, "message_id": message_id}
        return requests.post(url, json=payload).json()

    def send_photo(self, chat_id, photo_url, caption=""):
        """ إرسال صورة مع تعليق """
        url = f"{self.base_url}/sendPhoto"
        payload = {"chat_id": chat_id, "photo": photo_url, "caption": caption, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def send_video(self, chat_id, video_url, caption=""):
        """ إرسال فيديو مع تعليق """
        url = f"{self.base_url}/sendVideo"
        payload = {"chat_id": chat_id, "video": video_url, "caption": caption, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def send_audio(self, chat_id, audio_url, caption=""):
        """ إرسال ملف صوتي مع تعليق """
        url = f"{self.base_url}/sendAudio"
        payload = {"chat_id": chat_id, "audio": audio_url, "caption": caption, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def send_voice(self, chat_id, voice_url, caption=""):
        """ إرسال ملاحظة صوتية Voice Note """
        url = f"{self.base_url}/sendVoice"
        payload = {"chat_id": chat_id, "voice": voice_url, "caption": caption, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def send_animation(self, chat_id, animation_url, caption=""):
        """ إرسال GIF """
        url = f"{self.base_url}/sendAnimation"
        payload = {"chat_id": chat_id, "animation": animation_url, "caption": caption, "parse_mode": "HTML"}
        return requests.post(url, json=payload).json()

    def send_poll(self, chat_id, question, options, is_anonymous=True):
        """ إرسال استفتاء """
        url = f"{self.base_url}/sendPoll"
        payload = {"chat_id": chat_id, "question": question, "options": options, "is_anonymous": is_anonymous}
        return requests.post(url, json=payload).json()

    def send_contact(self, chat_id, phone_number, first_name, last_name=""):
        """ إرسال جهة اتصال """
        url = f"{self.base_url}/sendContact"
        payload = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name, "last_name": last_name}
        return requests.post(url, json=payload).json()

    def send_location(self, chat_id, latitude, longitude):
        """ إرسال موقع """
        url = f"{self.base_url}/sendLocation"
        payload = {"chat_id": chat_id, "latitude": latitude, "longitude": longitude}
        return requests.post(url, json=payload).json()

    def ban_chat_member(self, chat_id, user_id):
        """ حظر مستخدم من المجموعة """
        url = f"{self.base_url}/banChatMember"
        payload = {"chat_id": chat_id, "user_id": user_id}
        return requests.post(url, json=payload).json()

    def unban_chat_member(self, chat_id, user_id):
        """ إلغاء حظر مستخدم في المجموعة """
        url = f"{self.base_url}/unbanChatMember"
        payload = {"chat_id": chat_id, "user_id": user_id}
        return requests.post(url, json=payload).json()

    def restrict_chat_member(self, chat_id, user_id, until_date):
        """ تقييد مستخدم (منعه من الكتابة مثلاً) """
        url = f"{self.base_url}/restrictChatMember"
        payload = {"chat_id": chat_id, "user_id": user_id, "permissions": {"can_send_messages": False}, "until_date": until_date}
        return requests.post(url, json=payload).json()

    def promote_chat_member(self, chat_id, user_id, is_admin=True):
        """ ترقية مستخدم إلى مشرف """
        url = f"{self.base_url}/promoteChatMember"
        payload = {"chat_id": chat_id, "user_id": user_id, "can_manage_chat": is_admin}
        return requests.post(url, json=payload).json()

    def pin_chat_message(self, chat_id, message_id):
        """ تثبيت رسالة في القناة أو المجموعة """
        url = f"{self.base_url}/pinChatMessage"
        payload = {"chat_id": chat_id, "message_id": message_id}
        return requests.post(url, json=payload).json()

    def unpin_chat_message(self, chat_id, message_id=None):
        """ إزالة تثبيت رسالة معينة أو جميع الرسائل """
        url = f"{self.base_url}/unpinChatMessage"
        payload = {"chat_id": chat_id}
        if message_id:
            payload["message_id"] = message_id
        return requests.post(url, json=payload).json()