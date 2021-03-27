#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
using int64 = int64_t;

struct Point {
    int x;
    int y;

    bool operator==(const Point &other) const {
        return x==other.x && y==other.y;
    }
};

struct Edge {
    int x;
    int y;
    char dir; // D, U, L, R

    bool operator==(const Edge &other) const {
        return x==other.x && y==other.y && dir==other.dir;
    }

    bool operator!=(const Edge &other) const {
        return !((*this)==other);
    }
};

const int drx[4] =  {-1,  1,   0,   0};
const int dry[4] =  { 0,  0,   1,  -1};
const char dir[4] = {'U', 'D', 'R', 'L'};

class Task {
private:

    int n, m;
    vector<string> grid;
    vector<vector<bool>> visited;

    Point start, target;

    void read() {
        cin >> n >> m;
        string line;
        grid.resize(n);
        visited.resize(n, vector<bool>(m, false));
        for(int i = 0; i < n; ++i) {
            cin >> grid[i];
            for(int j = 0; j < m; ++j) {
                if(grid[i][j] == 'A') {
                    start = Point{i, j};
                } else if(grid[i][j] == 'B') {
                    target = Point{i, j};
                }
            }
        }
    }

    bool check_coordinate(const Point &p) {
        return 0 <= p.x && p.x < n && 0 <= p.y &&  p.y < m;
    }

    pair<int, string> bfs() {
        queue<Point> Queue;
        Queue.push(start);
        vector<vector<int>> dist(n, vector<int>(m, 1e9));

        Edge None = Edge{-1, -1, '?'};
        vector<vector<Edge>> prev(n, vector<Edge>(m, None));

        dist[start.x][start.y] = 0;
        visited[start.x][start.y] = true;

        bool found = false;
        while(!Queue.empty() && !found) {
            Point from = Queue.front(); Queue.pop();

            for(int i = 0; i < 4 && !found; ++i) {
                int new_x = from.x + drx[i];
                int new_y = from.y + dry[i];
                Point neighbor {new_x, new_y};
                char new_dir = dir[i];
                if(check_coordinate(neighbor) && !visited[new_x][new_y] && grid[new_x][new_y] != '#') {
                    Point new_point{neighbor.x, neighbor.y};
                    Queue.push(new_point);
                    visited[neighbor.x][neighbor.y] = true;
                    dist[new_point.x][new_point.y] = dist[from.x][from.y] + 1;
                    
                    prev[neighbor.x][neighbor.y] = Edge{from.x, from.y, new_dir};
                    
                    if(new_point == target) {
                        found = true;
                        break;
                    }
                }
            }
        }
        if(!found) {
            return make_pair(int(1e9), "");
        } else {
            string path="";
            Edge first = Edge{target.x, target.y, '?'};

            while(first != None) {
                first = prev[first.x][first.y];
                if(first == None)
                    break;
                path.push_back(first.dir);
            }
            reverse(path.begin(), path.end());
            return make_pair(dist[target.x][target.y], path);
        }
    }
    

    void solveOne() {
        auto [dist, path] = bfs();
        if(dist < 1e9) {
            cout << path << endl;
            return;
        } else {
            cout << "0 0\nNO" << endl;
        }
    }

public:
    void solve() {
        read();
        solveOne();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    Task solver;
    solver.solve();
    cout.flush();
    return 0;
}
