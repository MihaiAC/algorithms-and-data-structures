type Coord struct {
    x int
    y int
}

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
    var ddx = [...]int {-1, 1, 0, 0}
    var ddy = [...]int {0, 0, 1, -1}

    M := len(grid1)
    N := len(grid1[0])

    n_subislands := 0

    queue := make([]Coord, 0)

    for x := 0; x < M; x++ {
        for y := 0; y < N; y++ {
            if grid2[x][y] == 1 {
                grid2[x][y] = 0

                queue = append(queue, Coord{x, y})

                is_subisland := 1

                for len(queue) > 0 {
                    current_coord := queue[0]
                    queue = queue[1:]
                    cx, cy := current_coord.x, current_coord.y

                    if grid1[cx][cy] == 0 {
                        is_subisland = 0
                    }

                    for idx := range(ddx) {
                        dx, dy := ddx[idx], ddy[idx]
                        nx, ny := cx+dx, cy+dy
                        
                        if 0 <= nx && nx < M && 0 <= ny && ny < N && grid2[nx][ny] == 1 {
                            queue = append(queue, Coord{nx, ny})
                            grid2[nx][ny] = 0
                        }
                    }
                }

                n_subislands += is_subisland
            }
        }
    }

    return n_subislands
}