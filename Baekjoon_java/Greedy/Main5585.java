import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main5585 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int arr[] = {500, 100, 50, 10, 5, 1};
        int money = 1000 - Integer.parseInt(br.readLine());

        int count = 0;
        for (int change : arr) {
            if (money / change > 0) {
                count += money / change;
                money %= change;
            }
        }
        System.out.println(count);
    }
}
