from src.config_data.config import FABRIC_PRICES, ZIPPER_PRICE_PER_METER, WIDTH_OVERLAP
from src.lexicon.lexicon import ZIPPER_LABELS


def calculate_curtain_cost(fabric_type, height, width, zipper_count):
    fabric_price_per_m2 = FABRIC_PRICES[fabric_type]
    width_with_overlap = width + WIDTH_OVERLAP
    area = height * width_with_overlap
    fabric_cost = area * fabric_price_per_m2
    zipper_cost = height * zipper_count * ZIPPER_PRICE_PER_METER
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
        "total_cost": total_cost,
        "zipper_text": ZIPPER_LABELS[zipper_count],
        "zipper_cost_text": f"{zipper_cost}₽" if zipper_cost > 0 else "0₽"
    }
