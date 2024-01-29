class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Example usage
ball1 = Ball()
ball2 = Ball("super")

print(f"ball1.ball_type: {ball1.ball_type}")  # Output: "regular"
print(f"ball2.ball_type: {ball2.ball_type}")  # Output: "super"
