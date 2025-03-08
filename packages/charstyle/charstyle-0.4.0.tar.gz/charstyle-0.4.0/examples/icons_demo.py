#!/usr/bin/env python3
"""
Example of using the charstyle Icon enum.
This demonstrates how to use terminal icons for status indicators, progress bars,
and simple UI elements.
"""

from charstyle import (
    Icon,
    Style,
    styled,
    supports_color,
)


def main() -> None:
    """Main demo function for charstyle icons."""
    # Check if terminal supports colors
    if not supports_color():
        print("Your terminal doesn't support colors. Examples may not display correctly.")
        return

    print("\n=== charstyle Icons Demo ===\n")

    # Status indicators
    print(styled("Status Indicators:", Style.BOLD))
    print(f"{styled(Icon.CHECK, Style.GREEN)} {styled('Success:', Style.BOLD)} Operation completed")
    print(f"{styled(Icon.CROSS, Style.RED)} {styled('Error:', Style.BOLD)} File not found")
    print(
        f"{styled(Icon.WARNING, Style.YELLOW)} {styled('Warning:', Style.BOLD)} Disk space is low"
    )
    print(
        f"{styled(Icon.INFO, Style.BLUE)} {styled('Info:', Style.BOLD)} System is running normally"
    )
    print()

    # Progress bar with icons
    progress = 7
    bar = Icon.BLOCK * progress + Icon.LIGHT_SHADE * (10 - progress)
    print(styled("Progress Bar:", Style.BOLD))
    print(f"Loading: [{styled(bar, Style.GREEN)}] {progress * 10}%")
    print()

    # Box drawing with icons
    print(styled("Box Drawing:", Style.BOLD))
    print(f"{Icon.TOP_LEFT}{Icon.H_LINE * 20}{Icon.TOP_RIGHT}")
    print(f"{Icon.V_LINE} {styled('Menu', Style.BOLD)}               {Icon.V_LINE}")
    print(f"{Icon.T_RIGHT}{Icon.H_LINE * 20}{Icon.T_LEFT}")
    print(f"{Icon.V_LINE} {styled('1.', Style.GREEN)} New File        {Icon.V_LINE}")
    print(f"{Icon.V_LINE} {styled('2.', Style.GREEN)} Open File       {Icon.V_LINE}")
    print(f"{Icon.V_LINE} {styled('3.', Style.GREEN)} Save            {Icon.V_LINE}")
    print(f"{Icon.V_LINE} {styled('4.', Style.GREEN)} Exit            {Icon.V_LINE}")
    print(f"{Icon.BOTTOM_LEFT}{Icon.H_LINE * 20}{Icon.BOTTOM_RIGHT}")
    print()

    # Bullet points with icons
    print(styled("Bullet Points:", Style.BOLD))
    print(f"{Icon.CIRCLE} First item")
    print(f"{Icon.CIRCLE} Second item")
    print(f"{Icon.CIRCLE} Third item")
    print()

    # Arrows and directional indicators
    print(styled("Arrows:", Style.BOLD))
    print(f"{Icon.ARROW_RIGHT} Next")
    print(f"{Icon.ARROW_LEFT} Previous")
    print(f"{Icon.ARROW_UP} Up")
    print(f"{Icon.ARROW_DOWN} Down")
    print()

    # New emoji categories
    print(styled("Faces & People:", Style.BOLD))
    print(f"{Icon.FACE_GRINNING} {Icon.FACE_JOY} {Icon.FACE_SUNGLASSES} {Icon.FACE_THINKING}")
    print(f"{Icon.HAND_WAVE} {Icon.HAND_THUMBS_UP} {Icon.HAND_CLAP} {Icon.HAND_HEART}")
    print()

    print(styled("Nature & Animals:", Style.BOLD))
    print(f"{Icon.ANIMAL_DOG} {Icon.ANIMAL_CAT} {Icon.ANIMAL_PANDA} {Icon.ANIMAL_BUTTERFLY}")
    print(f"{Icon.ANIMAL_FISH} {Icon.ANIMAL_DOLPHIN} {Icon.ANIMAL_TIGER} {Icon.ANIMAL_KOALA}")
    print()

    print(styled("Food & Drink:", Style.BOLD))
    print(f"{Icon.FOOD_PIZZA} {Icon.FOOD_HAMBURGER} {Icon.FOOD_SUSHI} {Icon.FOOD_APPLE_RED}")
    print(f"{Icon.FOOD_BANANA} {Icon.FOOD_BROCCOLI} {Icon.FOOD_BREAD} {Icon.FOOD_HOTDOG}")
    print()

    print(styled("Activities & Objects:", Style.BOLD))
    print(f"{Icon.SPORT_SOCCER} {Icon.SPORT_BASKETBALL} {Icon.GAME_VIDEO_GAME} {Icon.MUSIC_GUITAR}")
    print(f"{Icon.SPORT_TENNIS} {Icon.GAME_DICE} {Icon.ART_ARTIST_PALETTE} {Icon.MUSIC_PIANO}")
    print()

    print(styled("Travel & Places:", Style.BOLD))
    print(
        f"{Icon.VEHICLE_CAR} {Icon.VEHICLE_AIRPLANE} {Icon.VEHICLE_ROCKET} {Icon.VEHICLE_BICYCLE}"
    )
    print(
        f"{Icon.VEHICLE_BUS} {Icon.VEHICLE_TRAIN} {Icon.VEHICLE_MOTORCYCLE} {Icon.VEHICLE_AMBULANCE}"
    )
    print()

    print(styled("Symbols:", Style.BOLD))
    print(
        f"{Icon.SYMBOL_RED_HEART} {Icon.SYMBOL_PEACE} {Icon.SYMBOL_YIN_YANG} {Icon.SYMBOL_STAR_OF_DAVID}"
    )
    print(
        f"{Icon.SYMBOL_GREEN_HEART} {Icon.SYMBOL_BLUE_HEART} {Icon.SYMBOL_PURPLE_HEART} {Icon.SYMBOL_BROKEN_HEART}"
    )
    print()

    print(styled("Flags:", Style.BOLD))
    print(f"{Icon.FLAG_USA} {Icon.FLAG_UK} {Icon.FLAG_JAPAN} {Icon.FLAG_RAINBOW}")
    print(f"{Icon.FLAG_CANADA} {Icon.FLAG_GERMANY} {Icon.FLAG_FRANCE} {Icon.FLAG_AUSTRALIA}")
    print()

    print(styled("Technical & Computing:", Style.BOLD))
    print(f"{Icon.TECH_SMARTPHONE} {Icon.TECH_COMPUTER} {Icon.TECH_LIGHT_BULB} {Icon.TECH_CAMERA}")
    print(f"{Icon.TECH_WATCH} {Icon.TECH_BATTERY} {Icon.TECH_PRINTER} {Icon.TECH_KEYBOARD}")
    print()


if __name__ == "__main__":
    main()
