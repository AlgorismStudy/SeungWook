import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main1012 {
    static boolean visited[][];
    static int M, N;
    static int arr[][];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i=0; i<T; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            arr = new int[M][N];
            visited = new boolean[M][N];

            for (int j=0; j<K; j++) {
                st = new StringTokenizer(br.readLine(), " ");
                int a = Integer.parseInt((st.nextToken()));
                int b = Integer.parseInt((st.nextToken()));
                arr[a][b] = 1;
            }
            
            int count = 0;
            for (int j=0; j<M; j++) {
                for (int k=0; k<N; k++) {
                    if (!visited[j][k] && arr[j][k] == 1) {
                        bfs(j, k);
                        count++;
                    }
                }
            }
            System.out.println(count);
        }
        br.close();
    }

    public static void bfs(int j, int k) {
        Queue<Integer> queuej = new LinkedList<>();
        Queue<Integer> queuek = new LinkedList<>();
        visited[j][k] = true;
        queuej.offer(j);
        queuek.offer(k);

        while (!queuej.isEmpty()) {
            int cur_j = queuej.poll();
            int cur_k = queuek.poll();

            int[] dx = {-1, 0, 1, 0};
            int[] dy = {0, 1, 0, -1};

            for (int i=0; i<4; i++) {
                int next_j = cur_j + dx[i];
                int next_k = cur_k + dy[i];

                if (next_j>=0 && next_j < M && next_k >=0 && next_k < N) {
                    if (!visited[next_j][next_k] && arr[next_j][next_k] == 1) {
                        visited[next_j][next_k] = true;
                        queuej.offer(next_j);
                        queuek.offer(next_k);
                    }
                }
            }
        }
    }
}
