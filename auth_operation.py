import sqlite3
import hashlib
import datetime


def authentification(id, password):
    """_summary_ : Authenticates the user and logs them in if the credentials are correct.

    Args:
        id (int): The id of the user.
        password (String): The password of the user in hashed form.

    Returns:
        int: 1 if the user is authenticated, 0 if the password is wrong, -1 if the user doesn't exist.
    """

    connection = sqlite3.connect("epet_database.db")
    cursor = connection.cursor()
    connection.commit()
    try:
        cursor.execute("SELECT * FROM user WHERE id = ?", (id,))
        user = cursor.fetchone()

        if user[1] == password and user[11] < 5:  # user[1] is the password column in the database
            cursor.execute(
                "UPDATE user SET login_attempts = 0 WHERE id = ?", (id,))
            connection.commit()
            return 1, user[10]  # Login successful and user type
        else:
            if user[11] == 4:
                cursor.execute(
                    "UPDATE user SET blocked_date = ? WHERE id = ?", (getDateTime(), id))
                cursor.execute(
                    "update user set login_attempts = login_attempts + 1 where id = ?", (id,))
                connection.commit()
                return -2, 0  # User is now blocked
            elif user[11] == 5:
                blocked_date = user[12]
                blocked_date = datetime.datetime.strptime(blocked_date, "%d-%m-%Y %H:%M")
                now = datetime.datetime.strptime(getDateTime(), "%d-%m-%Y %H:%M")
                
                if (now - blocked_date).total_seconds() > 300:           
                    # 5 minutes have passed since the user was blocked
                    print("5 minutes passed")
                    cursor.execute(
                        "UPDATE user SET blocked_date = ? WHERE id = ?", (None, id))
                    cursor.execute(
                        "UPDATE user SET login_attempts = 0 WHERE id = ?", (id,))
                    connection.commit()
                    if user[1] == password:
                        return 2, user[10]  # Login successful after being unblocked
                    else:
                        cursor.execute(
                            "update user set login_attempts = login_attempts + 1 where id = ?", (id,))
                        connection.commit()
                        return -4,0  # Wrong password after being unblocked
                return -3,0  # User is still blocked
            else:
                cursor.execute(
                    "update user set login_attempts = login_attempts + 1 where id = ?", (id,))
                connection.commit()
                return 0,0  # Wrong password
    except Exception as err:
        print(err)

    connection.close()
    return -1, 0  # Wrong ID or password





def getDateTime():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M")


