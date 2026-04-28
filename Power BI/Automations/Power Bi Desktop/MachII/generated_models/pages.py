
from __future__ import annotations

from typing import Any
from .base import page

# Leaf classes (no class-type dependencies)

class Pagedisplayoption(page):
    pass

class Bindingtype(page):
    pass

class Includealltypes(page):
    pass

class Queryaggregatefunction(page):
    pass

class Sortdirection(page):
    pass

class Querycomparisonkind(page):
    pass

class Timeunit(page):
    pass

class Arithmeticoperatorkind(page):
    pass

class Querynowexpression(page):
    pass

class Querydefaultvalueexpression(page):
    pass

class Queryallrolesrefexpression(page):
    pass

class Dataviewwildcardmatchingoption(page):
    pass

class Querytransformtablerefexpression(page):
    Source: str | None = None

class Querytransformoutputrolerefexpression(page):
    Role: str | None = None
    Transform: str | None = None

class Querynativevisualcalc(page):
    Language: str | None = None
    Expression: str | None = None
    Name: str | None = None
    DataType: str | None = None

class Queryrolerefexpression(page):
    Role: str | None = None

class Querysummaryvaluerefexpression(page):
    Name: str | None = None

class Queryselectrefexpression(page):
    ExpressionName: str | None = None

class Queryresourcepackageitem(page):
    PackageName: str | None = None
    PackageType: float | None = None
    ItemName: str | None = None

class Standalonesourcerefexpression(page):
    Schema: str | None = None
    Entity: str | None = None

class Querysourcerefexpression(page):
    Source: str | None = None

class Queryanyvalueexpression(page):
    DefaultValueOverridesAncestors: bool | None = None

class Queryliteralexpression(page):
    Value: str | None = None

class Queryexistsexpression(page):
    Expression: Queryexpressioncontainer | None = None

class Querynotexpression(page):
    Expression: Queryexpressioncontainer | None = None

class Querystartswithexpression(page):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querycontainsexpression(page):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querythemedatacolorexpression(page):
    ColorId: float | None = None
    Percent: float | None = None

class Queryvisualtopnexpression(page):
    ItemCount: float | None = None

class Dataviewwildcard(page):
    matchingOption: Dataviewwildcardmatchingoption | None = None

class Visualinteractionfiltertype(page):
    pass

class Annotation(page):
    name: str | None = None
    value: str | None = None

# Query expression related classes

class Queryminexpression(page):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Querymaxexpression(page):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryaggregationexpression(page):
    Function: Queryaggregatefunction | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydatespanexpression(page):
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydateaddexpression(page):
    Amount: float | None = None
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryarithmeticexpression(page):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None
    Operator: Arithmeticoperatorkind | None = None

class Querysortclause(page):
    Expression: Queryexpressioncontainer | None = None
    Direction: Sortdirection | None = None

class Querycomparisonexpression(page):
    ComparisonKind: Querycomparisonkind | None = None
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Queryfloorexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Size: float | None = None
    TimeUnit: float | None = None

class Querydiscretizeexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Count: float | None = None

class Querycolumnexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querymeasureexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Queryhierarchyexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Hierarchy: str | None = None

class Queryhierarchylevelexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Level: str | None = None

class Querypropertyvariationsourceexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Name: str | None = None
    Property: str | None = None

class Querybinaryexpression(page):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querybetweenexpression(page):
    Expression: Queryexpressioncontainer | None = None
    LowerBound: Queryexpressioncontainer | None = None
    UpperBound: Queryexpressioncontainer | None = None

class Queryinexpression(page):
    Expressions: list[Queryexpressioncontainer] | None = None
    Values: list[list[Queryexpressioncontainer]] | None = None
    Table: Queryexpressioncontainer | None = None

class Queryscopedevalexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Scope: list[Queryexpressioncontainer] | None = None

class Queryfilteredevalexpression(page):
    Expression: Queryexpressioncontainer | None = None
    Filters: list[Queryfilter] | None = None

class Querysparklinedataexpression(page):
    Measure: Queryexpressioncontainer | None = None
    Groupings: list[Queryexpressioncontainer] | None = None
    PointsPerSparkline: float | None = None
    ApplyCalculationGroupTo: str | None = None

class Queryfillruleexpression(page):
    Input: Queryexpressioncontainer | None = None
    FillRule: Any | None = None

class Querygrouprefexpression(page):
    GroupedColumns: list[Queryexpressioncontainer] | None = None
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querycase(page):
    Condition: Queryexpressioncontainer | None = None
    Value: Queryexpressioncontainer | None = None

class Queryconditionalexpression(page):
    Cases: list[Querycase] | None = None
    DefaultValue: Queryexpressioncontainer | None = None

class Queryexpressioncontentcache(page):
    Dependencies: list[Queryexpressioncontainer] | None = None
    UnrecognizedIdentifiers: bool | None = None

class Querynativemeasure(page):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querynativecolumn(page):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    Source: Queryexpressioncontainer | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querypercentileexpression(page):
    Expression: Queryexpressioncontainer | None = None
    K: float | None = None
    Exclusive: bool | None = None

# Core query expression container

class Queryexpressioncontainer(page):
    Name: str | None = None
    NativeReferenceName: str | None = None
    Annotations: dict[str, Any] | None = None
    SourceRef: Any | None = None
    Column: Querycolumnexpression | None = None
    Measure: Querymeasureexpression | None = None
    Min: Queryminexpression | None = None
    Max: Querymaxexpression | None = None
    Aggregation: Queryaggregationexpression | None = None
    Percentile: Querypercentileexpression | None = None
    Hierarchy: Queryhierarchyexpression | None = None
    HierarchyLevel: Queryhierarchylevelexpression | None = None
    PropertyVariationSource: Querypropertyvariationsourceexpression | None = None
    Subquery: Querysubqueryexpression | None = None
    Discretize: Querydiscretizeexpression | None = None
    And: Querybinaryexpression | None = None
    Between: Querybetweenexpression | None = None
    In: Queryinexpression | None = None
    Or: Querybinaryexpression | None = None
    Comparison: Querycomparisonexpression | None = None
    Not: Querynotexpression | None = None
    Contains: Querycontainsexpression | None = None
    StartsWith: Querystartswithexpression | None = None
    Exists: Queryexistsexpression | None = None
    Literal: Queryliteralexpression | None = None
    DateSpan: Querydatespanexpression | None = None
    DateAdd: Querydateaddexpression | None = None
    Now: Querynowexpression | None = None
    DefaultValue: Querydefaultvalueexpression | None = None
    AnyValue: Queryanyvalueexpression | None = None
    Arithmetic: Queryarithmeticexpression | None = None
    Floor: Queryfloorexpression | None = None
    ScopedEval: Queryscopedevalexpression | None = None
    FilteredEval: Queryfilteredevalexpression | None = None
    TransformTableRef: Querytransformtablerefexpression | None = None
    TransformOutputRoleRef: Querytransformoutputrolerefexpression | None = None
    SparklineData: Querysparklinedataexpression | None = None
    NativeVisualCalculation: Querynativevisualcalc | None = None
    FillRule: Queryfillruleexpression | None = None
    GroupRef: Querygrouprefexpression | None = None
    ResourcePackageItem: Queryresourcepackageitem | None = None
    RoleRef: Queryrolerefexpression | None = None
    SummaryValueRef: Querysummaryvaluerefexpression | None = None
    AllRolesRef: Queryallrolesrefexpression | None = None
    SelectRef: Queryselectrefexpression | None = None
    ThemeDataColor: Querythemedatacolorexpression | None = None
    Conditional: Queryconditionalexpression | None = None
    NativeMeasure: Querynativemeasure | None = None
    NativeColumn: Querynativecolumn | None = None
    VisualTopN: Queryvisualtopnexpression | None = None

# Filter and definition classes

class Queryfilter(page):
    Target: list[Queryexpressioncontainer] | None = None
    Condition: Queryexpressioncontainer | None = None
    Annotations: dict[str, Any] | None = None

class Entitysource(page):
    Name: str | None = None
    Entity: str | None = None
    Schema: str | None = None
    Expression: Queryexpressioncontainer | None = None
    Type: float | None = None

class Querydefinition(page):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None
    OrderBy: list[Querysortclause] | None = None
    Select: list[Queryexpressioncontainer] | None = None
    VisualShape: list[Axis] | None = None
    GroupBy: list[Queryexpressioncontainer] | None = None
    Transform: list[Querytransform] | None = None
    Top: float | None = None

class Querysubqueryexpression(page):
    Query: Querydefinition | None = None

# Transform and axis related classes

class Querytransformtablecolumn(page):
    Role: str | None = None
    Expression: Queryexpressioncontainer | None = None

class Querytransformtable(page):
    Name: str | None = None
    Columns: list[Querytransformtablecolumn] | None = None

class Querytransformoutput(page):
    Table: Querytransformtable | None = None

class Querytransforminput(page):
    Parameters: list[Queryexpressioncontainer] | None = None
    Table: Querytransformtable | None = None

class Querytransform(page):
    Name: str | None = None
    Algorithm: str | None = None
    Input: Querytransforminput | None = None
    Output: Querytransformoutput | None = None

class Axisgroup(page):
    Keys: list[Queryexpressioncontainer] | None = None
    Subtotal: bool | None = None

class Axis(page):
    Groups: list[Axisgroup] | None = None
    Name: str | None = None

# Page binding classes

class Bindingparameter(page):
    name: str | None = None
    boundFilter: str | None = None
    asAggregation: bool | None = None
    qnaSingleSelectRequired: bool | None = None
    fieldExpr: Queryexpressioncontainer | None = None

class Pagebinding(page):
    name: str | None = None
    type: Bindingtype | None = None
    referenceScope: str | None = None
    parameters: list[Bindingparameter] | None = None
    acceptsFilterContext: str | None = None

# Selector and data model classes

class Datarepetitionselector(page):
    scopeId: Queryexpressioncontainer | None = None
    wildcard: list[Queryexpressioncontainer] | None = None
    roles: list[str] | None = None
    total: list[Queryexpressioncontainer] | None = None
    dataViewWildcard: Dataviewwildcard | None = None

class Selector(page):
    data: list[Datarepetitionselector] | None = None
    metadata: str | None = None
    id: str | None = None
    highlightMatching: float | None = None
    hierarchyMatching: float | None = None
    order: float | None = None

# Page formatting classes

class Pageinformation(page):
    pageInformationName: Any | None = None
    pageInformationQnaPodEnabled: Any | None = None
    pageInformationAltName: Any | None = None
    pageInformationType: Any | None = None

class Pagesize(page):
    pageSizeTypes: Any | None = None
    pageSizeWidth: Any | None = None
    pageSizeHeight: Any | None = None

class Background(page):
    color: Any | None = None
    image: Any | None = None
    transparency: Any | None = None

class Displayarea(page):
    verticalAlignment: Any | None = None

class Outspacepane(page):
    backgroundColor: Any | None = None
    transparency: Any | None = None
    foregroundColor: Any | None = None
    titleSize: Any | None = None
    searchTextSize: Any | None = None
    headerSize: Any | None = None
    fontFamily: Any | None = None
    border: Any | None = None
    borderColor: Any | None = None
    checkboxAndApplyColor: Any | None = None
    inputBoxColor: Any | None = None
    width: Any | None = None

class Filtercard(page):
    backgroundColor: Any | None = None
    transparency: Any | None = None
    border: Any | None = None
    borderColor: Any | None = None
    foregroundColor: Any | None = None
    textSize: Any | None = None
    fontFamily: Any | None = None
    inputBoxColor: Any | None = None

class Pagerefresh(page):
    show: Any | None = None
    refreshType: Any | None = None
    duration: Any | None = None
    dialogLauncher: Any | None = None
    measure: Any | None = None
    checkEvery: Any | None = None

class Personalizevisual(page):
    show: Any | None = None
    perspectiveRef: Any | None = None
    applyToAllPages: Any | None = None

class PageformattingobjectsPageinformationItem(page):
    selector: Selector | None = None
    properties: Pageinformation | None = None

class PageformattingobjectsPagesizeItem(page):
    selector: Selector | None = None
    properties: Pagesize | None = None

class PageformattingobjectsBackgroundItem(page):
    selector: Selector | None = None
    properties: Background | None = None

class PageformattingobjectsDisplayareaItem(page):
    selector: Selector | None = None
    properties: Displayarea | None = None

class PageformattingobjectsOutspaceItem(page):
    selector: Selector | None = None
    properties: Background | None = None

class PageformattingobjectsOutspacepaneItem(page):
    selector: Selector | None = None
    properties: Outspacepane | None = None

class PageformattingobjectsFiltercardItem(page):
    selector: Selector | None = None
    properties: Filtercard | None = None

class PageformattingobjectsPagerefreshItem(page):
    selector: Selector | None = None
    properties: Pagerefresh | None = None

class PageformattingobjectsPersonalizevisualItem(page):
    selector: Selector | None = None
    properties: Personalizevisual | None = None

class Pageformattingobjects(page):
    pageInformation: list[dict[str, Any]] | None = None
    pageSize: list[dict[str, Any]] | None = None
    background: list[dict[str, Any]] | None = None
    displayArea: list[dict[str, Any]] | None = None
    outspace: list[dict[str, Any]] | None = None
    outspacePane: list[dict[str, Any]] | None = None
    filterCard: list[dict[str, Any]] | None = None
    pageRefresh: list[dict[str, Any]] | None = None
    personalizeVisual: list[dict[str, Any]] | None = None

# Visual interaction classes

class Visualinteraction(page):
    source: str | None = None
    target: str | None = None
    type: Visualinteractionfiltertype | None = None

# Auto page generation classes

class Quickexplorevisualcontainerconfig(page):
    name: str | None = None
    fields: list[Queryexpressioncontainer] | None = None

class Quickexplorerelatedlayout(page):
    version: float | None = None
    dataTableName: str | None = None

class Quickexplorecombinationlayout(page):
    version: float | None = None
    dataTableName: str | None = None

class Quickexplorelayoutcontainer(page):
    related: Quickexplorerelatedlayout | None = None
    combination: Quickexplorecombinationlayout | None = None

class Autopagegenerationconfig(page):
    selectedFields: list[Queryexpressioncontainer] | None = None
    visualContainerConfigurations: list[Quickexplorevisualcontainerconfig] | None = None
    layout: Quickexplorelayoutcontainer | None = None

# Filter configuration classes

class Filterdefinition(page):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None

class Filtercontainerformattingobjectsproperties(page):
    requireSingleSelect: Any | None = None
    isInvertedSelectionMode: Any | None = None

class FiltercontainerObjectsGeneralItem(page):
    selector: Selector | None = None
    properties: Filtercontainerformattingobjectsproperties | None = None

class Filtercontainerformattingobjects(page):
    general: list[dict[str, Any]] | None = None

class Filtercontainer(page):
    name: str | None = None
    displayName: str | None = None
    ordinal: float | None = None
    field: Queryexpressioncontainer | None = None
    type: str | None = None
    filter: Filterdefinition | None = None
    restatement: str | None = None
    howCreated: str | None = None
    isHiddenInViewMode: bool | None = None
    isLockedInViewMode: bool | None = None
    objects: Filtercontainerformattingobjects | None = None

class RootFilterconfig(page):
    filters: list[Filtercontainer] | None = None
    filterSortOrder: str | None = None
