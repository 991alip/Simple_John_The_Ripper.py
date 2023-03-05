import hashlib
import argparse

parser = argparse.ArgumentParser(description='Simple John The Rip>
parser.add_argument('hash_type', type=str, help='Hash type (md5, >
parser.add_argument('password_hash', type=str, help='Password has>
parser.add_argument('dictionary_file', type=str, help='Dictionary>

args = parser.parse_args()

def check_password(password):
    if args.hash_type == 'md5':
        hash_object = hashlib.md5(password.encode())
    elif args.hash_type == 'sha1':
        hash_object = hashlib.sha1(password.encode())
    elif args.hash_type == 'sha256':
        hash_object = hashlib.sha256(password.encode())
    elif args.hash_type == 'sha512':
        hash_object = hashlib.sha512(password.encode())
    else:
        print("Invalid hash type!")
        return False

    if hash_object.hexdigest() == args.password_hash:
        print("Password found: ", password)
        return True
    return False

with open(args.dictionary_file, "r", errors='ignore') as f:
    for line in f:
        password = line.strip()
