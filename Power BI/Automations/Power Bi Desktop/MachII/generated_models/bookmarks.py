
from __future__ import annotations

from typing import Any
from .base import bookmark

# Leaf classes (no class-type dependencies)

class Includealltypes(bookmark):
    pass

class Queryaggregatefunction(bookmark):
    pass

class Sortdirection(bookmark):
    pass

class Querycomparisonkind(bookmark):
    pass

class Timeunit(bookmark):
    pass

class Arithmeticoperatorkind(bookmark):
    pass

class Querynowexpression(bookmark):
    pass

class Querydefaultvalueexpression(bookmark):
    pass

class Queryallrolesrefexpression(bookmark):
    pass

class Dataviewobjectdefinitions(bookmark):
    pass

class Projectionstate(bookmark):
    pass

class Parameterstatebyrole(bookmark):
    pass

class Visualcontainerdisplaymode(bookmark):
    pass

class Dataviewwildcardmatchingoption(bookmark):
    pass

class Querytransformtablerefexpression(bookmark):
    Source: str | None = None

class Querytransformoutputrolerefexpression(bookmark):
    Role: str | None = None
    Transform: str | None = None

class Querynativevisualcalc(bookmark):
    Language: str | None = None
    Expression: str | None = None
    Name: str | None = None
    DataType: str | None = None

class Queryrolerefexpression(bookmark):
    Role: str | None = None

class Querysummaryvaluerefexpression(bookmark):
    Name: str | None = None

class Queryselectrefexpression(bookmark):
    ExpressionName: str | None = None

class Queryresourcepackageitem(bookmark):
    PackageName: str | None = None
    PackageType: float | None = None
    ItemName: str | None = None

class Standalonesourcerefexpression(bookmark):
    Schema: str | None = None
    Entity: str | None = None

class Querysourcerefexpression(bookmark):
    Source: str | None = None

class Queryanyvalueexpression(bookmark):
    DefaultValueOverridesAncestors: bool | None = None

class Queryliteralexpression(bookmark):
    Value: str | None = None

class Queryexistsexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None

class Querynotexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None

class Querystartswithexpression(bookmark):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querycontainsexpression(bookmark):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querythemedatacolorexpression(bookmark):
    ColorId: float | None = None
    Percent: float | None = None

class Queryvisualtopnexpression(bookmark):
    ItemCount: float | None = None

class Selectorsforcolumn(bookmark):
    pass

class VisualcontainerstateSinglevisualDisplayMaximizedoptions(bookmark):
    dataTable: str | None = None

class ExplorationstateFiltersByexprItemFilterexpressionmetadataAnyof0Jsonfilter(bookmark):
    filterType: Any | None = None

class ExplorationstateFiltersByexprItemFilterexpressionmetadataAnyof1Jsonfilter(bookmark):
    filterType: Any | None = None

# Classes depending on leaf classes

class Queryminexpression(bookmark):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Querymaxexpression(bookmark):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryaggregationexpression(bookmark):
    Function: Queryaggregatefunction | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydatespanexpression(bookmark):
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydateaddexpression(bookmark):
    Amount: float | None = None
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryarithmeticexpression(bookmark):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None
    Operator: Arithmeticoperatorkind | None = None

class Querysortclause(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Direction: Sortdirection | None = None

class Querycomparisonexpression(bookmark):
    ComparisonKind: Querycomparisonkind | None = None
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Queryfloorexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Size: float | None = None
    TimeUnit: float | None = None

class Querydiscretizeexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Count: float | None = None

# Query expression container and related nested structures

class Querycolumnexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querymeasureexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Queryhierarchyexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Hierarchy: str | None = None

class Queryhierarchylevelexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Level: str | None = None

class Querypropertyvariationsourceexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Name: str | None = None
    Property: str | None = None

class Querybinaryexpression(bookmark):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querybetweenexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    LowerBound: Queryexpressioncontainer | None = None
    UpperBound: Queryexpressioncontainer | None = None

class Queryinexpression(bookmark):
    Expressions: list[Queryexpressioncontainer] | None = None
    Values: list[list[Queryexpressioncontainer]] | None = None
    Table: Queryexpressioncontainer | None = None

class Queryscopedevalexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Scope: list[Queryexpressioncontainer] | None = None

class Queryfilteredevalexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    Filters: list[Queryfilter] | None = None

class Querysparklinedataexpression(bookmark):
    Measure: Queryexpressioncontainer | None = None
    Groupings: list[Queryexpressioncontainer] | None = None
    PointsPerSparkline: float | None = None
    ApplyCalculationGroupTo: str | None = None

class Queryfillruleexpression(bookmark):
    Input: Queryexpressioncontainer | None = None
    FillRule: Any | None = None

class Querygrouprefexpression(bookmark):
    GroupedColumns: list[Queryexpressioncontainer] | None = None
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querycase(bookmark):
    Condition: Queryexpressioncontainer | None = None
    Value: Queryexpressioncontainer | None = None

class Queryconditionalexpression(bookmark):
    Cases: list[Querycase] | None = None
    DefaultValue: Queryexpressioncontainer | None = None

class Queryexpressioncontentcache(bookmark):
    Dependencies: list[Queryexpressioncontainer] | None = None
    UnrecognizedIdentifiers: bool | None = None

class Querynativemeasure(bookmark):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querynativecolumn(bookmark):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    Source: Queryexpressioncontainer | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Queryexpressioncontainer(bookmark):
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

class Querypercentileexpression(bookmark):
    Expression: Queryexpressioncontainer | None = None
    K: float | None = None
    Exclusive: bool | None = None

class Querysubqueryexpression(bookmark):
    Query: Querydefinition | None = None

class Queryfilter(bookmark):
    Target: list[Queryexpressioncontainer] | None = None
    Condition: Queryexpressioncontainer | None = None
    Annotations: dict[str, Any] | None = None

class Querydefinition(bookmark):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None
    OrderBy: list[Querysortclause] | None = None
    Select: list[Queryexpressioncontainer] | None = None
    VisualShape: list[Axis] | None = None
    GroupBy: list[Queryexpressioncontainer] | None = None
    Transform: list[Querytransform] | None = None
    Top: float | None = None

class Entitysource(bookmark):
    Name: str | None = None
    Entity: str | None = None
    Schema: str | None = None
    Expression: Queryexpressioncontainer | None = None
    Type: float | None = None

# Higher-level state and filter classes

class Filterlabelidpair(bookmark):
    id: Datarepetitionselector | None = None
    displayName: str | None = None

class Dataviewwildcard(bookmark):
    matchingOption: Dataviewwildcardmatchingoption | None = None

class Datarepetitionselector(bookmark):
    scopeId: Queryexpressioncontainer | None = None
    wildcard: list[Queryexpressioncontainer] | None = None
    roles: list[str] | None = None
    total: list[Queryexpressioncontainer] | None = None
    dataViewWildcard: Dataviewwildcard | None = None

class Identityvaluemap(bookmark):
    identities: list[Datarepetitionselector] | None = None
    valueMap: dict[str, Any] | None = None

class Filterexpressionmetadata(bookmark):
    expressions: list[Queryexpressioncontainer] | None = None
    cachedValueItems: list[Identityvaluemap] | None = None
    jsonFilter: dict[str, Any] | None = None

class DecomposedtreeQueryexpressioncontainer(bookmark):
    left: DecomposedtreeQueryexpressioncontainer | None = None
    right: DecomposedtreeQueryexpressioncontainer | None = None
    value: Queryexpressioncontainer | None = None

class Decomposedidentities(bookmark):
    values: list[list[dict[str, Any]]] | None = None
    columns: list[DecomposedtreeQueryexpressioncontainer] | None = None

class Decomposedfilterexpressionmetadata(bookmark):
    decomposedIdentities: Decomposedidentities | None = None
    expressions: list[Any] | None = None
    valueMap: list[dict[str, Any]] | None = None
    jsonFilter: dict[str, Any] | None = None

class Filtercontainerstate(bookmark):
    name: str | None = None
    type: str | None = None
    filter: Filterdefinition | None = None
    expression: Queryexpressioncontainer | None = None
    restatement: str | None = None
    howCreated: float | None = None
    precedence: float | None = None
    isTransient: bool | None = None
    cachedDisplayNames: list[Filterlabelidpair] | None = None
    filterExpressionMetadata: Any | None = None

class Filterdefinition(bookmark):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None

class Filtersstate(bookmark):
    byName: dict[str, Any] | None = None
    byExpr: list[Filtercontainerstate] | None = None
    byType: list[Filtercontainerstate] | None = None
    byTransientState: list[Filtercontainerstate] | None = None

class Bookmarkoptions(bookmark):
    applyOnlyToTargetVisuals: bool | None = None
    targetVisualNames: list[str] | None = None
    suppressActiveSection: bool | None = None
    suppressData: bool | None = None
    suppressDisplay: bool | None = None

# Transform and axis related classes

class Querytransformtablecolumn(bookmark):
    Role: str | None = None
    Expression: Queryexpressioncontainer | None = None

class Querytransformtable(bookmark):
    Name: str | None = None
    Columns: list[Querytransformtablecolumn] | None = None

class Querytransformoutput(bookmark):
    Table: Querytransformtable | None = None

class Querytransforminput(bookmark):
    Parameters: list[Queryexpressioncontainer] | None = None
    Table: Querytransformtable | None = None

class Querytransform(bookmark):
    Name: str | None = None
    Algorithm: str | None = None
    Input: Querytransforminput | None = None
    Output: Querytransformoutput | None = None

class Axisgroup(bookmark):
    Keys: list[Queryexpressioncontainer] | None = None
    Subtotal: bool | None = None

class Axis(bookmark):
    Groups: list[Axisgroup] | None = None
    Name: str | None = None

# Data view and selector classes

class Dataviewobjectpropertyidwithselector(bookmark):
    object: str | None = None
    property: str | None = None
    selector: Selector | None = None

class Selector(bookmark):
    data: list[Datarepetitionselector] | None = None
    metadata: str | None = None
    id: str | None = None
    highlightMatching: float | None = None
    hierarchyMatching: float | None = None
    order: float | None = None

class Dataviewobjectdefinitionupdates(bookmark):
    merge: Dataviewobjectdefinitions | None = None
    remove: list[Dataviewobjectpropertyidwithselector] | None = None

# Section and visual container states

class Sectionstate(bookmark):
    filters: Filtersstate | None = None
    visualContainers: dict[str, Any] | None = None
    visualContainerGroups: dict[str, Any] | None = None

class Highlightstate(bookmark):
    selection: Any | None = None
    filterExpressionMetadata: Any | None = None

class Singlevisualconfigstate(bookmark):
    visualType: str | None = None
    autoSelectVisualType: bool | None = None
    targetType: str | None = None
    targetAutoSelectVisualType: bool | None = None
    objects: Dataviewobjectdefinitionupdates | None = None
    orderBy: list[Querysortclause] | None = None
    activeProjections: Projectionstate | None = None
    projections: Projectionstate | None = None
    parameters: Parameterstatebyrole | None = None
    display: Visualcontainerdisplaystate | None = None
    cachedFilterDisplayItems: list[Filterlabelidpair] | None = None
    expansionStates: list[Any] | None = None
    filterExpressionMetadata: Any | None = None
    isDrillDisabled: bool | None = None

class Visualcontainerdisplaystate(bookmark):
    mode: Visualcontainerdisplaymode | None = None
    maximizedOptions: dict[str, Any] | None = None

class Visualcontainerstate(bookmark):
    filters: Filtersstate | None = None
    singleVisual: Singlevisualconfigstate | None = None
    highlight: Highlightstate | None = None

# Decomposed state classes

class Selectorsbycolumn(bookmark):
    dataMap: Selectorsforcolumn | None = None
    metadata: list[str] | None = None
    id: str | None = None

class Decomposedselectors(bookmark):
    decomposedIdentities: Decomposedidentities | None = None
    queryNameMap: list[dict[str, Any]] | None = None
    queryNames: list[str] | None = None
    metadata: list[list[str]] | None = None
    id: list[str] | None = None

class Parameterstate(bookmark):
    expr: Queryexpressioncontainer | None = None
    index: float | None = None
    length: float | None = None
    sortDirection: float | None = None

class Visualcontainergroupstate(bookmark):
    isHidden: bool | None = None
    children: dict[str, Any] | None = None

class Explorationstate(bookmark):
    version: str | None = None
    activeSection: str | None = None
    filters: Filtersstate | None = None
    sections: dict[str, Any] | None = None
    objects: Dataviewobjectdefinitionupdates | None = None
    dataSourceVariables: str | None = None
