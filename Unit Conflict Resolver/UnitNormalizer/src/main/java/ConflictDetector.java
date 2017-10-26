import nl.wur.fbr.om.model.units.Unit;

/**
 * Created by nuwantha on 9/4/17.
 */
public class ConflictDetector {

    private Unit unit;
    private Unit baseUnit;
    private int unitTokenNumber;
    private int valueTokenNumber;
    private String category;
    private String valueToken;


    public Unit getUnit() {
        return unit;
    }

    public void setUnit(Unit unit) {
        this.unit = unit;
    }

    public int getValueTokenNumber() {
        return valueTokenNumber;
    }

    public void setValueTokenNumber(int valueTokenNumber) {
        this.valueTokenNumber = valueTokenNumber;
    }

    public Unit getBaseUnit() {
        return baseUnit;
    }

    public void setBaseUnit(Unit baseUnit) {
        this.baseUnit = baseUnit;
    }

    public int getUnitTokenNumber() {
        return unitTokenNumber;
    }

    public void setUnitTokenNumber(int unitTokenNumber) {
        this.unitTokenNumber = unitTokenNumber;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getValueToken() {
        return valueToken;
    }

    public void setValueToken(String valueToken) {
        this.valueToken = valueToken;
    }
}
