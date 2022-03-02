import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main1072 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        
        long X = Long.parseLong(st.nextToken());
        long Y = Long.parseLong(st.nextToken());
        long Z = (Y * 100) / X;

        long start = 0;
        long end = 1000000001;
        long mid, temp;

        if (Z >= 99) {
            System.out.print("-1");
        } else {
            while (start <= end) {
                mid = (start+end) / 2;
                temp = ((Y+mid)*100) / (X+mid);
                if  (temp > Z) {
                    end = mid -1;
                } else start = mid + 1;
            }
            System.out.print(start);
        }
    }
}
