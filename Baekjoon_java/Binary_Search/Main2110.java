import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main2110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int arr[] = new int[N];
        for (int i=0; i<arr.length; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }
        br.close();
        Arrays.sort(arr);

        int start = 1;
        int end = arr[N-1] - arr[0];
        int mid = (start+end) / 2;

        int result = 1;
        while(start <= end) {
            int count = 1;
            int tmp = arr[0];
            for(int i=1; i<arr.length; i++) {
                int distance = arr[i] - tmp;
                if (distance >= mid) {
                    tmp = arr[i];
                    count++;
                } 
            }
            if (count >= C) {
                result = Math.max(result, mid);
                start = mid + 1;
            } else end = mid - 1;
            mid = (start + end) / 2;
        }
        System.out.print(result);
    }
}

