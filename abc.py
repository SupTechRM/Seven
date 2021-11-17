import json

credentials = {
  "type": "service_account",
  "project_id": "empyrean-app-332014",
  "private_key_id": "6fdfdc87b1dfc464e3d435c1ff670ae428959e27",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDsPmQTlLhB1cOA\nb1gr350bFyS++XeTqP/kQz9DRlE3sWIMQwn7iaDwtdDgNQz0CaJzbLM3pc5R3kF4\ngrwmIXPsDPpB8TFfODdyjF+jqcwnDdhentVv1GKGHwzI8Cu69Ty0UNjUokI3APxt\n0uMIyq1ebuGLve0OXclEc+AKcaXrK1dTWFChpcL3IbeI4BYBup+C9DYNQckMKfVI\n3ulCvRGLhOE449UbNGiY0XK4hOmUjWIzdJ2KvtBJH+2fOn7QxnF9ChuxhWyMYVwr\n9/KcNiyLODCbUPSiZ0T3Jylj+k0jHcyirlUsqKHUYbxvnFwgceCBXuxIgwojxnzC\nxPI49dPNAgMBAAECggEADXtSArwN99PXIFE6Wuab9JvRgQSDim2ujLw5tAEjSWZa\nDhEVVMF56cK2dNUSNCsIlkWxxI81wv5IBjSPwC1QjDwBXBoDk0eGAod4PcLG38Ou\ngVfXHlakeLr049Kw7C5qlG+4sAnCdZkczremNS47zpPNU0g3awZ3Iezq8C2kJlNq\nyY5pfYUOxi5b505LJBzYbr5uBd7BI4vlunK4pksKCjqYBavlX8Tv3dgbui5C4xRs\nQZwBKovXIvp3Ha/S+JLg42g+hX6Rj/PkKQgCEWHja/7ZVk7ePU2wQ/QdntuGOOl1\nuHLNoP+RiyM/pYGLBeo25yR9oK/W62DmAdEiW7loEQKBgQD6fzqESuq3JiAgVm+5\nBUWfiCaqEjU7aVu2s86AHNGonKKUtKmeil2jwp/J33fyR8QafashqBY61n7i5X9c\nJ1eAjPhnuEHKBPdTDpQD0G6js1jRPnv7d4Kmu9sq1/HZQ2T4ZTTfviEJfvGELm0I\nLj6tl6thlIO09u6LhxIs2JuZowKBgQDxbwDXS5q30Bt1Z/PkWdKZ4bEE+nK/TzoI\ne9gSAuUW+ylU/G4GrJunWZ4/07ZfhlSwKU+6aQYbak42P7Cvo9SxiMUuhAEqtQns\n2cBDk+2JiSMu0kbV1gVdxug5e8z2/iKbtRZ503qNeG4c0sNqbz2ME+hU9VWbDAAY\neVyDVSSTzwKBgQDy9aX/HF7NpzfvxYZ1UUy3MCo4OJLS/hyLd5ipn8omnU3/p78A\n27l5FVNATPQc1Ui6XPs4GLz+8n59ehTuf+YZ9CEXEJsW43wzXedoT6iQNGrIAK/m\nNoNNTtWDl5GmpfxwBFGlVdbbS/nat+De12PJoVsDuTWJtxulzytsvecluwKBgQDp\nHYQTXWXLW75Xk4LTlsMZX+jbZLNM80OWk3Wilnb6xJI5A+98tEcqxAZfnJ04CO1W\nltzroaKK8A8KpF6GiMrCjMvPSRgTU3B86BeTaI7vwKFfARvyNs9Bp9/sORRD3Egw\nTh6gjMiFNqYjYIHdEAG+ci5fce8xYNnqx6vDB3/k0wKBgQChdqx8MgVIk/w24IXd\nPPq4OTIIeAKN9Eyr5GIWnU2GuMN7DL5WcSHwnZVOeBquIyfpVAXwbWsLau3GuAJv\ne9AWyAJLVshEymCMEn7mD8tjPfNiWcUqnjzjuT2CHzprv7h3AGpzjIYgxadpGUdN\n8w2xKjZbS/K/4o6soJjJNjqRWA==\n-----END PRIVATE KEY-----\n",
  "client_email": "seventexttospeech@empyrean-app-332014.iam.gserviceaccount.com",
  "client_id": "108636702627397812418",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/seventexttospeech%40empyrean-app-332014.iam.gserviceaccount.com"
}

with open("something.json", "w") as fp:
  json.dump(credentials, fp)