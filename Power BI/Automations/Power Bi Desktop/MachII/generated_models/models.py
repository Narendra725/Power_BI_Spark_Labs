from __future__ import annotations

from typing import Any
from .base import BaseSchema

# Leaf classes (no class-type dependencies)

class Themeresourcepackagetype(BaseSchema):
    pass

class Themeversion(BaseSchema):
    visual: str | None = None
    page: str | None = None
    report: str | None = None

class Thememetadata(BaseSchema):
    name: str | None = None
    reportVersionAtImport: Themeversion | None = None
    type: Themeresourcepackagetype | None = None

class Themecollection(BaseSchema):
    baseTheme: Thememetadata | None = None
    customTheme: Thememetadata | None = None

# Simple leaf classes with no dependencies

class Includealltypes(BaseSchema):
    pass

class Queryaggregatefunction(BaseSchema):
    pass

class Sortdirection(BaseSchema):
    pass

class Querycomparisonkind(BaseSchema):
    pass

class Timeunit(BaseSchema):
    pass

class Arithmeticoperatorkind(BaseSchema):
    pass

class Querynowexpression(BaseSchema):
    pass

class Querydefaultvalueexpression(BaseSchema):
    pass

class Queryallrolesrefexpression(BaseSchema):
    pass

class Dataviewwildcardmatchingoption(BaseSchema):
    pass

class Querytransformtablerefexpression(BaseSchema):
    Source: str | None = None

class Querytransformoutputrolerefexpression(BaseSchema):
    Role: str | None = None
    Transform: str | None = None

class Querynativevisualcalc(BaseSchema):
    Language: str | None = None
    Expression: str | None = None
    Name: str | None = None
    DataType: str | None = None

class Queryrolerefexpression(BaseSchema):
    Role: str | None = None

class Querysummaryvaluerefexpression(BaseSchema):
    Name: str | None = None

class Queryselectrefexpression(BaseSchema):
    ExpressionName: str | None = None

class Queryresourcepackageitem(BaseSchema):
    PackageName: str | None = None
    PackageType: float | None = None
    ItemName: str | None = None

class Standalonesourcerefexpression(BaseSchema):
    Schema: str | None = None
    Entity: str | None = None

class Querysourcerefexpression(BaseSchema):
    Source: str | None = None

class Queryanyvalueexpression(BaseSchema):
    DefaultValueOverridesAncestors: bool | None = None

class Queryliteralexpression(BaseSchema):
    Value: str | None = None

class Queryexistsexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None

class Querynotexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None

class Querystartswithexpression(BaseSchema):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querycontainsexpression(BaseSchema):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querythemedatacolorexpression(BaseSchema):
    ColorId: float | None = None
    Percent: float | None = None

class Queryvisualtopnexpression(BaseSchema):
    ItemCount: float | None = None

class Dataviewwildcard(BaseSchema):
    matchingOption: Dataviewwildcardmatchingoption | None = None

class Outspacepane(BaseSchema):
    expanded: Any | None = None
    visible: Any | None = None

class Section(BaseSchema):
    verticalAlignment: Any | None = None

class Resourcepackagetype(BaseSchema):
    pass

class Resourcepackageitemtype(BaseSchema):
    pass

class Annotation(BaseSchema):
    name: str | None = None
    value: str | None = None

# Query expression related classes

class Queryminexpression(BaseSchema):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Querymaxexpression(BaseSchema):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryaggregationexpression(BaseSchema):
    Function: Queryaggregatefunction | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydatespanexpression(BaseSchema):
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydateaddexpression(BaseSchema):
    Amount: float | None = None
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryarithmeticexpression(BaseSchema):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None
    Operator: Arithmeticoperatorkind | None = None

class Querysortclause(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Direction: Sortdirection | None = None

class Querycomparisonexpression(BaseSchema):
    ComparisonKind: Querycomparisonkind | None = None
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Queryfloorexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Size: float | None = None
    TimeUnit: float | None = None

class Querydiscretizeexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Count: float | None = None

class Querycolumnexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querymeasureexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Queryhierarchyexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Hierarchy: str | None = None

class Queryhierarchylevelexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Level: str | None = None

class Querypropertyvariationsourceexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Name: str | None = None
    Property: str | None = None

class Querybinaryexpression(BaseSchema):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querybetweenexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    LowerBound: Queryexpressioncontainer | None = None
    UpperBound: Queryexpressioncontainer | None = None

class Queryinexpression(BaseSchema):
    Expressions: list[Queryexpressioncontainer] | None = None
    Values: list[list[Queryexpressioncontainer]] | None = None
    Table: Queryexpressioncontainer | None = None

class Queryscopedevalexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Scope: list[Queryexpressioncontainer] | None = None

class Queryfilteredevalexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    Filters: list[Queryfilter] | None = None

class Querysparklinedataexpression(BaseSchema):
    Measure: Queryexpressioncontainer | None = None
    Groupings: list[Queryexpressioncontainer] | None = None
    PointsPerSparkline: float | None = None
    ApplyCalculationGroupTo: str | None = None

class Queryfillruleexpression(BaseSchema):
    Input: Queryexpressioncontainer | None = None
    FillRule: Any | None = None

class Querygrouprefexpression(BaseSchema):
    GroupedColumns: list[Queryexpressioncontainer] | None = None
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querycase(BaseSchema):
    Condition: Queryexpressioncontainer | None = None
    Value: Queryexpressioncontainer | None = None

class Queryconditionalexpression(BaseSchema):
    Cases: list[Querycase] | None = None
    DefaultValue: Queryexpressioncontainer | None = None

class Queryexpressioncontentcache(BaseSchema):
    Dependencies: list[Queryexpressioncontainer] | None = None
    UnrecognizedIdentifiers: bool | None = None

class Querynativemeasure(BaseSchema):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querynativecolumn(BaseSchema):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    Source: Queryexpressioncontainer | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querypercentileexpression(BaseSchema):
    Expression: Queryexpressioncontainer | None = None
    K: float | None = None
    Exclusive: bool | None = None

# Core query expression container

class Queryexpressioncontainer(BaseSchema):
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

class Queryfilter(BaseSchema):
    Target: list[Queryexpressioncontainer] | None = None
    Condition: Queryexpressioncontainer | None = None
    Annotations: dict[str, Any] | None = None

class Entitysource(BaseSchema):
    Name: str | None = None
    Entity: str | None = None
    Schema: str | None = None
    Expression: Queryexpressioncontainer | None = None
    Type: float | None = None

class Querydefinition(BaseSchema):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None
    OrderBy: list[Querysortclause] | None = None
    Select: list[Queryexpressioncontainer] | None = None
    VisualShape: list[Axis] | None = None
    GroupBy: list[Queryexpressioncontainer] | None = None
    Transform: list[Querytransform] | None = None
    Top: float | None = None

class Querysubqueryexpression(BaseSchema):
    Query: Querydefinition | None = None

# Transform and axis related classes

class Querytransformtablecolumn(BaseSchema):
    Role: str | None = None
    Expression: Queryexpressioncontainer | None = None

class Querytransformtable(BaseSchema):
    Name: str | None = None
    Columns: list[Querytransformtablecolumn] | None = None

class Querytransformoutput(BaseSchema):
    Table: Querytransformtable | None = None

class Querytransforminput(BaseSchema):
    Parameters: list[Queryexpressioncontainer] | None = None
    Table: Querytransformtable | None = None

class Querytransform(BaseSchema):
    Name: str | None = None
    Algorithm: str | None = None
    Input: Querytransforminput | None = None
    Output: Querytransformoutput | None = None

class Axisgroup(BaseSchema):
    Keys: list[Queryexpressioncontainer] | None = None
    Subtotal: bool | None = None

class Axis(BaseSchema):
    Groups: list[Axisgroup] | None = None
    Name: str | None = None

# Selector and data model classes

class Datarepetitionselector(BaseSchema):
    scopeId: Queryexpressioncontainer | None = None
    wildcard: list[Queryexpressioncontainer] | None = None
    roles: list[str] | None = None
    total: list[Queryexpressioncontainer] | None = None
    dataViewWildcard: Dataviewwildcard | None = None

class Selector(BaseSchema):
    data: list[Datarepetitionselector] | None = None
    metadata: str | None = None
    id: str | None = None
    highlightMatching: float | None = None
    hierarchyMatching: float | None = None
    order: float | None = None

# Formatting and resource classes

class Resourcepackageitem(BaseSchema):
    id: float | None = None
    name: str | None = None
    path: str | None = None
    type: Resourcepackageitemtype | None = None

class Resourcepackage(BaseSchema):
    id: float | None = None
    name: str | None = None
    type: Resourcepackagetype | None = None
    items: list[Resourcepackageitem] | None = None
    disabled: bool | None = None

class Organizationcustomvisual(BaseSchema):
    name: str | None = None
    path: str | None = None
    disabled: bool | None = None

class ReportformattingobjectsOutspacepaneItem(BaseSchema):
    selector: Selector | None = None
    properties: Outspacepane | None = None

class ReportformattingobjectsSectionItem(BaseSchema):
    selector: Selector | None = None
    properties: Section | None = None

class Reportformattingobjects(BaseSchema):
    outspacePane: list[dict[str, Any]] | None = None
    section: list[dict[str, Any]] | None = None

# Filter configuration classes

class Filterdefinition(BaseSchema):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None

class Filtercontainerformattingobjectsproperties(BaseSchema):
    requireSingleSelect: Any | None = None
    isInvertedSelectionMode: Any | None = None

class FiltercontainerObjectsGeneralItem(BaseSchema):
    selector: Selector | None = None
    properties: Filtercontainerformattingobjectsproperties | None = None

class Filtercontainerformattingobjects(BaseSchema):
    general: list[dict[str, Any]] | None = None

class Filtercontainer(BaseSchema):
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

class RootFilterconfig(BaseSchema):
    filters: list[Filtercontainer] | None = None
    filterSortOrder: str | None = None

# Settings classes

class Explorationsettings(BaseSchema):
    isPersistentUserStateDisabled: bool | None = None
    hideVisualContainerHeader: bool | None = None
    useStylableVisualContainerHeader: bool | None = None
    exportDataMode: str | None = None
    isReportAnnotationsDisabled: bool | None = None
    defaultFilterActionIsDataFilter: bool | None = None
    defaultDrillFilterOtherVisuals: bool | None = None
    useCrossReportDrillthrough: bool | None = None
    allowChangeFilterTypes: bool | None = None
    allowInlineExploration: bool | None = None
    useEnhancedTooltips: bool | None = None
    useScaledTooltips: bool | None = None
    filterPaneHiddenInEditMode: bool | None = None
    disableFilterPaneSearch: bool | None = None
    pagesPosition: str | None = None
    allowAutomatedInsightsNotification: bool | None = None
    useDefaultAggregateDisplayName: bool | None = None
    enableDeveloperMode: bool | None = None
    pauseQueries: bool | None = None
    queryLimitOption: str | None = None
    customMemoryLimit: str | None = None
    customTimeoutLimit: str | None = None

class Explorationslowdatasourcesettings(BaseSchema):
    isCrossHighlightingDisabled: bool | None = None
    isSlicerSelectionsButtonEnabled: bool | None = None
    isFilterSelectionsButtonEnabled: bool | None = None
    isFieldWellButtonEnabled: bool | None = None
    isApplyAllButtonEnabled: bool | None = None
