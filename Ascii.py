
from PIL import Image
from collections import deque

# ---------- CONFIG ----------
ASCII_CHARS = "@%#*+=-:."
INTENSITY_THRESHOLD = 15
SMALL_REGION_SIZE = 15

MAX_WIDTH = 55
ASCII_RATIO = 0.5
# ----------------------------

def load_grayscale(path):
    img = Image.open(path).convert("L")
    aspect_ratio = img.height / img.width
    new_height = int(MAX_WIDTH * aspect_ratio * ASCII_RATIO)
    img = img.resize((MAX_WIDTH, new_height))
    return img

#Main Logic to track node as pixels
def bfs_region(img, visited, start_r, start_c):
    rows, cols = img.size[1], img.size[0]
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True

    region = [(start_r, start_c)]
    base_intensity = img.getpixel((start_c, start_r))

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                intensity = img.getpixel((nc, nr))
                if abs(intensity - base_intensity) <= INTENSITY_THRESHOLD:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    region.append((nr, nc))
    return region

#Mapping 
def map_to_ascii(intensity, region_size):
    # pixel-accurate mapping (same logic as simple ASCII version)
    idx = intensity * len(ASCII_CHARS) // 256
    char = ASCII_CHARS[idx]

    # subtle region refinement (eyes/details)
    if intensity < 60 and region_size < SMALL_REGION_SIZE:
        char = '@'

    return char


def generate_ascii_art(path):
    img = load_grayscale(path)
    rows, cols = img.size[1], img.size[0]

    visited = [[False]*cols for _ in range(rows)]
    ascii_grid = [[' ']*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region = bfs_region(img, visited, r, c)
                region_size = len(region)

                for rr, cc in region:
                    intensity = img.getpixel((cc, rr))
                    ascii_grid[rr][cc] = map_to_ascii(intensity, region_size)

    # PRINT RESULT
    for r in range(rows):
        for c in range(cols):
            print(ascii_grid[r][c], end='')
        print()


# ---------- RUN ----------
generate_ascii_art(
    r"" #Just enter your image path here
)

