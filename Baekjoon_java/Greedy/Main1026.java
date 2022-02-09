import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main1026 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine(), " ");
        int arr1[] = new int[N];
        for (int i=0; i<N; i++) {
            arr1[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr1);
        
        st = new StringTokenizer(br.readLine(), " ");
        Integer arr2[] = new Integer[N];
        for (int i=0; i<N; i++) {
            arr2[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr2, Collections.reverseOrder());

        br.close();

        int result = 0;
        for (int i=0; i<N; i++) {
            result += (arr1[i] * arr2[i]);
        }

        System.out.println(result);
    }
}
