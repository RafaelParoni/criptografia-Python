from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def gerar_chaves(): 
    # Gerar um par de chaves RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key
       
def criptografar_mensagem(public_key, mensagem):
    print('Criptografando mensagem: ')
    # Criptografar a mensagem
    ciphertext = public_key.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def descriptografar_mensagem(private_key, ciphertext):
    print('Descriptografando a mensagem: ')
    # Descriptografar a mensagem
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()


# Gerar chaves
private_key, public_key = gerar_chaves()

# Mensagem a ser criptografada
    
print('Digite um texto para ser criptografado:')
mensagem = input("-> ")

# Criptografar a mensagem
ciphertext = criptografar_mensagem(public_key, mensagem)
print("-> ", ciphertext)

# Descriptografar a mensagem
decrypted_message = descriptografar_mensagem(private_key, ciphertext)
print("-> ", decrypted_message)

