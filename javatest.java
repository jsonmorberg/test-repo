import java.util.*;

public class SampleTest {
    int a = 5;

    public static void main(String args[]) {
        System.out.println("The value is: " + 42);

        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        for (int i = 0; i < names.size(); i++) {
            System.out.println("Name: " + names.get(i));
        }

        if (names != null && !names.isEmpty()) {
            System.out.println("Names list is not empty");
        }

        try {
            int result = divide(10, 0);
        } catch (Exception e) {
        }
    }

    public static int divide(int x, int y) {
        return x / y;
    }
}
