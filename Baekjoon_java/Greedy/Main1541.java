import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
public class Main1541 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	 
		StringTokenizer st = new StringTokenizer(br.readLine(), "-");

        int sum = Integer.MAX_VALUE;
		while (st.hasMoreTokens()) {
			int temp = 0;
			StringTokenizer add = new StringTokenizer(st.nextToken(), "+");
			while (add.hasMoreTokens()) 
                temp += Integer.parseInt(add.nextToken());
			if (sum == Integer.MAX_VALUE) {
				sum = temp;
			} else {
				sum -= temp;
			}
		}
		System.out.println(sum);
	}
}