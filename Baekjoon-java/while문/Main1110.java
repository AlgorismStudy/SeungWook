import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        br.close();

        if (N < 10) N *= 11;

        int New_N = Integer.parseInt(String.valueOf(N%10) + String.valueOf((N/10 + N%10)%10));

        int count = 1;
        while (N != New_N) {
            New_N = Integer.parseInt(String.valueOf(New_N%10) + String.valueOf((New_N/10 + New_N%10)%10));
            count++;
        }
        System.out.println(count);
    }
}
