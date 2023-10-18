# hiddy_delete
حذف کننده اشتراک هیدیفای

برای استفاده باید مقدار uuid را مشخص کنید و app.py ران شود

خیلی راحت از این کد توی هر باتی استفاده کنید.
### حتما در صورت رضایت ⭐star⭐ بدهید.


# مثال
<pre>
```python
from user_deleter import get_id, delete_user_by_id
import requests

if __name__ == "__main__":
    link_panel = 'https://example.com/eqfrnr0n890_9e3-9/b3c4a23qdwa0-9271-rqwf;pked0k=23-m'
    target_uuid = "odcpwd_9031-0a-d0ciocap23"
    with requests.Session() as session:
        user_id_to_delete = get_id(session, target_uuid, f"{link_panel}/admin/user/")
        if user_id_to_delete:
            result = delete_user_by_id(session, link_panel, user_id_to_delete)
            print(result)
```
</pre>
