import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main11000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
    
        PriorityQueue<Integer> start = new PriorityQueue<>();
        PriorityQueue<Integer> end = new PriorityQueue<>();    
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            start.offer(Integer.parseInt(st.nextToken()));
            end.offer(Integer.parseInt(st.nextToken()));
        }
        br.close();

        int max = 0;
        int count = 0;
        while(!start.isEmpty()) {
            int tmp = start.poll();
            while (tmp >= end.peek()) {
                end.poll();
                count--;
            }
            max = Math.max(max, ++count);
        }
        System.out.print(max);
    }
}
