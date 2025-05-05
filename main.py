from password_cracker import crack_sha1_hash
import test_module

def main():
    # Test without salts
    print("Testing without salts:")
    print(crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec"))  # should return "sammy123"
    print(crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e"))  # should return "abacab"
    print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"))  # should return "password"
    
    # Test with salts
    print("\nTesting with salts:")
    print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True))  # should return "superman"
    print(crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", True))  # should return "q1w2e3r4t5"
    print(crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True))  # should return "bubbles1"
    
    # Run unit tests
    print("\nRunning unit tests...")
    test_module.run_tests()

if __name__ == "__main__":
    main()