// vars/greetUser.groovy
def call(String name = 'Guest') {
    echo "Hello, ${name}! Welcome to Jenkins shared libraries!"
}
