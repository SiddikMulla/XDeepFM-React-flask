
# Dictionary containing user information (email, password, user_id)
users = {
    'user1@example.com': {'password': 'password', 'user_id': 'AHPAXGZTH4KAGQHOWQ4SGU4BN23Q'},
    'user2@example.com': {'password': 'password', 'user_id': 'AGPH5EGCVPZPPTMO5OM5DGVYEMLA'},
    'user3@example.com': {'password': 'password', 'user_id': 'AFRY27GPRRTESTN746JGSGNPGW5Q'},
    'user4@example.com': {'password': 'password', 'user_id': 'AE3PLZHW6NXWBMZ76TDVFQG2MJFA'},
    'user5@example.com': {'password': 'password', 'user_id': 'AFOHSZOUYV4P3STMGY3ZVWEQAFQQ'},
    # Add more users as needed
}

def validate_credentials(email, password):
    # Check if the user exists and the password matches
    if email in users and users[email]['password'] == password:
        # Return the user ID if credentials are valid
        return users[email]['user_id']
    else:
        # Return None if authentication fails
        return None