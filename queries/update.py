
update_user_email_query = """
update User
set email='%s'
where user_id=%s;
"""