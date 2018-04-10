public class HelloWorld {
	private static final long PRINT_DELAY = 1000L;
	private String name = "world";
	private void bar(String howdy) {
        // howdy is not used
    }
    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        System.out.println("Hello, World");
    }
    public void test(){
    	    // unusual use of branching statement in a loop
		for (int i = 0; i < 10; i++) {
		    if (i*i <= 25) {
		        continue;
		    }
		    break;
		}

		// this makes more sense...
		for (int i = 0; i < 10; i++) {
		    if (i*i > 25) {
		        break;
		    }
		}
    }

}