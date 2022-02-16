import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2606 {
    static int N;
    static int[][] graph;
    static boolean[] visit;
    static int count = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        
        graph = new int[N+1][N+1];
        visit = new boolean[N+1]; 
        
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt((st.nextToken()));
            int b = Integer.parseInt((st.nextToken()));
            graph[a][b] = graph[b][a] = 1;
        }
        br.close();

        dfs(1);
        System.out.println(count - 1);
    }
    public static void dfs(int start) {
        visit[start] = true;
        count++;

        for(int i=0; i<=N; i++) {
            if(graph[start][i] == 1 && !visit[i]) dfs(i);
        }
    }
}
