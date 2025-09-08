
import secrets 

def generate_secret_key( ) -> str : 

    return secrets.token_urlsafe(32) 


if __name__ == "__main__" : 
    print( " new secret key : " , generate_secret_key() )