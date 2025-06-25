import pytest
import math

# --- Function to be tested ---
def calculate_projectile_range(initial_velocity: float, launch_angle_degrees: float) -> float:
    """
    Calculates the horizontal range of a projectile given initial velocity and launch angle.
    """
    if initial_velocity < 0 or launch_angle_degrees < 0 or launch_angle_degrees > 90:
        raise ValueError("Invalid input: velocity and angle must be non-negative, angle <= 90.")

    g = 9.80665
    angle_radians = math.radians(launch_angle_degrees)
    range_val = (initial_velocity**2 * math.sin(2 * angle_radians)) / g
    return max(0.0, range_val)


# --- Fixtures ---
@pytest.fixture
def default_velocity():
    """Provides a default velocity for tests."""
    return 10.0

@pytest.fixture
def default_gravity():
    """Returns gravity constant for manual calculations (not used directly in function)."""
    return 9.80665


# --- Individual Tests ---
def test_zero_velocity():
    assert calculate_projectile_range(0, 45) == 0.0

def test_valid_angle(default_velocity, default_gravity):
    expected_range = (default_velocity**2 * math.sin(2 * math.radians(45))) / default_gravity
    assert calculate_projectile_range(default_velocity, 45) == pytest.approx(expected_range)

def test_negative_velocity_raises():
    with pytest.raises(ValueError, match="Invalid input"):
        calculate_projectile_range(-10, 45)

def test_angle_too_high_raises():
    with pytest.raises(ValueError, match="Invalid input"):
        calculate_projectile_range(10, 100)

def test_negative_angle_raises():
    with pytest.raises(ValueError, match="Invalid input"):
        calculate_projectile_range(10, -5)


# --- Parametrized Testing ---
@pytest.mark.parametrize("velocity, angle, expected", [
    (10, 45, 10.197),
    (20, 30, 35.31),
    (5, 0, 0.0),
    (5, 90, 0.0),
])
def test_projectile_range_cases(velocity, angle, expected):
    assert calculate_projectile_range(velocity, angle) == pytest.approx(expected, abs=0.01)
