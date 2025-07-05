#!/usr/bin/env python3
"""
Test script for curtain cost calculation logic
"""


# Test calculation logic
def calculate_curtain_cost(fabric_type, height, width, zipper_count):
    """Calculate curtain cost based on parameters"""

    # Fabric prices per square meter
    fabric_prices = {
        "Брезент": 500,
        "Оксфорд": 450
    }

    # Zipper price per linear meter
    zipper_price_per_meter = 300

    # Overlap for width calculation
    width_overlap = 0.1

    # Calculate costs
    fabric_price_per_m2 = fabric_prices[fabric_type]
    width_with_overlap = width + width_overlap
    area = height * width_with_overlap
    fabric_cost = area * fabric_price_per_m2

    # Calculate zipper cost
    zipper_cost = height * zipper_count * zipper_price_per_meter

    # Total cost
    total_cost = fabric_cost + zipper_cost

    return {
        "fabric_type": fabric_type,
        "height": height,
        "width": width,
        "width_with_overlap": width_with_overlap,
        "area": area,
        "fabric_cost": fabric_cost,
        "zipper_count": zipper_count,
        "zipper_cost": zipper_cost,
        "total_cost": total_cost
    }


def format_result(result):
    """Format calculation result as bot would display it"""
    zipper_text = {
        0: "Без молнии",
        1: "1 шт. по центру",
        2: "2 шт. по бокам"
    }[result["zipper_count"]]

    zipper_cost_text = f"{result['zipper_cost']}₽" if result['zipper_cost'] > 0 else "0₽"

    return (
        f"🧾 Расчёт стоимости шторы:\n\n"
        f"Ткань: {result['fabric_type']}\n"
        f"Размер: {result['height']} м (высота) x {result['width']} м (ширина)\n"
        f"С учётом припуска: {result['width_with_overlap']} м\n"
        f"Площадь: {result['area']:.1f} м²\n"
        f"Стоимость ткани: {result['fabric_cost']:,.0f}₽\n"
        f"Молния: {zipper_text} — {zipper_cost_text}\n"
        f"✅ Итоговая стоимость: {result['total_cost']:,.0f}₽"
    )


if __name__ == "__main__":
    # Test with example from requirements
    test_result = calculate_curtain_cost("Брезент", 3, 3.8, 1)
    print("Тестовый расчёт:")
    print(format_result(test_result))

    print("\n" + "=" * 50 + "\n")

    # Test with Oxford fabric
    test_result2 = calculate_curtain_cost("Оксфорд", 2.5, 4.2, 2)
    print("Дополнительный тест:")
    print(format_result(test_result2))
