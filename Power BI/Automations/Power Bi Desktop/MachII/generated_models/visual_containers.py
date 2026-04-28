
from __future__ import annotations

from typing import Any
from .base import visualContainer

# Leaf classes (no class-type dependencies)

class Grouplayoutmode(visualContainer):
    pass

class Includealltypes(visualContainer):
    pass

class Queryaggregatefunction(visualContainer):
    pass

class Sortdirection(visualContainer):
    pass

class Querycomparisonkind(visualContainer):
    pass

class Timeunit(visualContainer):
    pass

class Arithmeticoperatorkind(visualContainer):
    pass

class Querynowexpression(visualContainer):
    pass

class Querydefaultvalueexpression(visualContainer):
    pass

class Queryallrolesrefexpression(visualContainer):
    pass

class Dataviewwildcardmatchingoption(visualContainer):
    pass

class Querytransformtablerefexpression(visualContainer):
    Source: str | None = None

class Querytransformoutputrolerefexpression(visualContainer):
    Role: str | None = None
    Transform: str | None = None

class Querynativevisualcalc(visualContainer):
    Language: str | None = None
    Expression: str | None = None
    Name: str | None = None
    DataType: str | None = None

class Queryrolerefexpression(visualContainer):
    Role: str | None = None

class Querysummaryvaluerefexpression(visualContainer):
    Name: str | None = None

class Queryselectrefexpression(visualContainer):
    ExpressionName: str | None = None

class Queryresourcepackageitem(visualContainer):
    PackageName: str | None = None
    PackageType: float | None = None
    ItemName: str | None = None

class Standalonesourcerefexpression(visualContainer):
    Schema: str | None = None
    Entity: str | None = None

class Querysourcerefexpression(visualContainer):
    Source: str | None = None

class Queryanyvalueexpression(visualContainer):
    DefaultValueOverridesAncestors: bool | None = None

class Queryliteralexpression(visualContainer):
    Value: str | None = None

class Queryexistsexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None

class Querynotexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None

class Querystartswithexpression(visualContainer):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querycontainsexpression(visualContainer):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querythemedatacolorexpression(visualContainer):
    ColorId: float | None = None
    Percent: float | None = None

class Queryvisualtopnexpression(visualContainer):
    ItemCount: float | None = None

class Dataviewwildcard(visualContainer):
    matchingOption: Dataviewwildcardmatchingoption | None = None

class Dataviewobjectdefinitions(visualContainer):
    pass

class Projectionstate(visualContainer):
    pass

class Aidecompositionmethod(visualContainer):
    pass

class Annotation(visualContainer):
    name: str | None = None
    value: str | None = None

# Query expression related classes

class Queryminexpression(visualContainer):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Querymaxexpression(visualContainer):
    IncludeAllTypes: Includealltypes | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryaggregationexpression(visualContainer):
    Function: Queryaggregatefunction | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydatespanexpression(visualContainer):
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Querydateaddexpression(visualContainer):
    Amount: float | None = None
    TimeUnit: Timeunit | None = None
    Expression: Queryexpressioncontainer | None = None

class Queryarithmeticexpression(visualContainer):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None
    Operator: Arithmeticoperatorkind | None = None

class Querysortclause(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Direction: Sortdirection | None = None

class Querycomparisonexpression(visualContainer):
    ComparisonKind: Querycomparisonkind | None = None
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Queryfloorexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Size: float | None = None
    TimeUnit: float | None = None

class Querydiscretizeexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Count: float | None = None

class Querycolumnexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querymeasureexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Queryhierarchyexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Hierarchy: str | None = None

class Queryhierarchylevelexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Level: str | None = None

class Querypropertyvariationsourceexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Name: str | None = None
    Property: str | None = None

class Querybinaryexpression(visualContainer):
    Left: Queryexpressioncontainer | None = None
    Right: Queryexpressioncontainer | None = None

class Querybetweenexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    LowerBound: Queryexpressioncontainer | None = None
    UpperBound: Queryexpressioncontainer | None = None

class Queryinexpression(visualContainer):
    Expressions: list[Queryexpressioncontainer] | None = None
    Values: list[list[Queryexpressioncontainer]] | None = None
    Table: Queryexpressioncontainer | None = None

class Queryscopedevalexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Scope: list[Queryexpressioncontainer] | None = None

class Queryfilteredevalexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    Filters: list[Queryfilter] | None = None

class Querysparklinedataexpression(visualContainer):
    Measure: Queryexpressioncontainer | None = None
    Groupings: list[Queryexpressioncontainer] | None = None
    PointsPerSparkline: float | None = None
    ApplyCalculationGroupTo: str | None = None

class Queryfillruleexpression(visualContainer):
    Input: Queryexpressioncontainer | None = None
    FillRule: Any | None = None

class Querygrouprefexpression(visualContainer):
    GroupedColumns: list[Queryexpressioncontainer] | None = None
    Expression: Queryexpressioncontainer | None = None
    Property: str | None = None

class Querycase(visualContainer):
    Condition: Queryexpressioncontainer | None = None
    Value: Queryexpressioncontainer | None = None

class Queryconditionalexpression(visualContainer):
    Cases: list[Querycase] | None = None
    DefaultValue: Queryexpressioncontainer | None = None

class Queryexpressioncontentcache(visualContainer):
    Dependencies: list[Queryexpressioncontainer] | None = None
    UnrecognizedIdentifiers: bool | None = None

class Querynativemeasure(visualContainer):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querynativecolumn(visualContainer):
    DataType: float | None = None
    Expression: str | None = None
    Language: str | None = None
    Source: Queryexpressioncontainer | None = None
    ExpressionContentCache: Queryexpressioncontentcache | None = None
    ProposedName: str | None = None
    Format: str | None = None

class Querypercentileexpression(visualContainer):
    Expression: Queryexpressioncontainer | None = None
    K: float | None = None
    Exclusive: bool | None = None

# Core query expression container

class Queryexpressioncontainer(visualContainer):
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

class Queryfilter(visualContainer):
    Target: list[Queryexpressioncontainer] | None = None
    Condition: Queryexpressioncontainer | None = None
    Annotations: dict[str, Any] | None = None

class Entitysource(visualContainer):
    Name: str | None = None
    Entity: str | None = None
    Schema: str | None = None
    Expression: Queryexpressioncontainer | None = None
    Type: float | None = None

class Querydefinition(visualContainer):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None
    OrderBy: list[Querysortclause] | None = None
    Select: list[Queryexpressioncontainer] | None = None
    VisualShape: list[Axis] | None = None
    GroupBy: list[Queryexpressioncontainer] | None = None
    Transform: list[Querytransform] | None = None
    Top: float | None = None

class Querysubqueryexpression(visualContainer):
    Query: Querydefinition | None = None

# Transform and axis related classes

class Querytransformtablecolumn(visualContainer):
    Role: str | None = None
    Expression: Queryexpressioncontainer | None = None

class Querytransformtable(visualContainer):
    Name: str | None = None
    Columns: list[Querytransformtablecolumn] | None = None

class Querytransformoutput(visualContainer):
    Table: Querytransformtable | None = None

class Querytransforminput(visualContainer):
    Parameters: list[Queryexpressioncontainer] | None = None
    Table: Querytransformtable | None = None

class Querytransform(visualContainer):
    Name: str | None = None
    Algorithm: str | None = None
    Input: Querytransforminput | None = None
    Output: Querytransformoutput | None = None

class Axisgroup(visualContainer):
    Keys: list[Queryexpressioncontainer] | None = None
    Subtotal: bool | None = None

class Axis(visualContainer):
    Groups: list[Axisgroup] | None = None
    Name: str | None = None

# Visual container position and group config

class Visualcontainerposition(visualContainer):
    x: float | None = None
    y: float | None = None
    z: float | None = None
    height: float | None = None
    width: float | None = None
    tabOrder: float | None = None
    angle: float | None = None

class Background(visualContainer):
    show: Any | None = None
    color: Any | None = None
    transparency: Any | None = None

class Lockaspect(visualContainer):
    show: Any | None = None

class Visualgroupgeneralformattingobjects(visualContainer):
    x: Any | None = None
    y: Any | None = None
    width: Any | None = None
    height: Any | None = None
    altText: Any | None = None

class VisualgroupconfigObjectsBackgroundItem(visualContainer):
    selector: Selector | None = None
    properties: Background | None = None

class VisualgroupconfigObjectsLockaspectItem(visualContainer):
    selector: Selector | None = None
    properties: Lockaspect | None = None

class VisualgroupconfigObjectsGeneralItem(visualContainer):
    selector: Selector | None = None
    properties: Visualgroupgeneralformattingobjects | None = None

class Visualgroupformattingobjects(visualContainer):
    background: list[dict[str, Any]] | None = None
    lockAspect: list[dict[str, Any]] | None = None
    general: list[dict[str, Any]] | None = None

class Visualgroupconfig(visualContainer):
    displayName: str | None = None
    groupMode: Grouplayoutmode | None = None
    objects: Visualgroupformattingobjects | None = None

# Selector and data model classes

class Datarepetitionselector(visualContainer):
    scopeId: Queryexpressioncontainer | None = None
    wildcard: list[Queryexpressioncontainer] | None = None
    roles: list[str] | None = None
    total: list[Queryexpressioncontainer] | None = None
    dataViewWildcard: Dataviewwildcard | None = None

class Selector(visualContainer):
    data: list[Datarepetitionselector] | None = None
    metadata: str | None = None
    id: str | None = None
    highlightMatching: float | None = None
    hierarchyMatching: float | None = None
    order: float | None = None

# Query and sort classes

class Querysort(visualContainer):
    field: Queryexpressioncontainer | None = None
    direction: Sortdirection | None = None

class Sortdefinition(visualContainer):
    sort: list[Querysort] | None = None
    isDefaultSort: bool | None = None

class Visualqueryoptions(visualContainer):
    allowBinnedLineSample: bool | None = None
    allowOverlappingPointsSample: bool | None = None

class Query(visualContainer):
    sortDefinition: Sortdefinition | None = None
    options: Visualqueryoptions | None = None
    queryState: dict[str, Any] | None = None
    isDrillDisabled: bool | None = None

# Projection and role classes

class Roleprojection(visualContainer):
    field: Queryexpressioncontainer | None = None
    queryRef: str | None = None
    nativeQueryRef: str | None = None
    displayName: str | None = None
    format: str | None = None
    active: bool | None = None
    hidden: bool | None = None

class Rolefieldparameter(visualContainer):
    parameterExpr: Queryexpressioncontainer | None = None
    index: float | None = None
    length: float | None = None
    sortDirection: str | None = None

# Expansion state classes

class Nodeexpansionstate(visualContainer):
    identityValues: list[Queryexpressioncontainer] | None = None
    isToggled: bool | None = None
    children: list[Nodeexpansionstate] | None = None

class Rootexpansionstate(visualContainer):
    identityValues: list[Queryexpressioncontainer] | None = None
    isToggled: bool | None = None
    children: list[Nodeexpansionstate] | None = None

class Ailevelinformation(visualContainer):
    method: Aidecompositionmethod | None = None
    disabled: bool | None = None

class Levelexpansionstate(visualContainer):
    identityKeys: list[Queryexpressioncontainer] | None = None
    isCollapsed: bool | None = None
    queryRefs: list[str] | None = None
    isPinned: bool | None = None
    isLocked: bool | None = None
    AIInformation: Ailevelinformation | None = None

class Expansionstate(visualContainer):
    roles: list[str] | None = None
    root: Rootexpansionstate | None = None
    levels: list[Levelexpansionstate] | None = None

# Visual sync group

class Visualsyncgroup(visualContainer):
    groupName: str | None = None
    fieldChanges: bool | None = None
    filterChanges: bool | None = None

# Visual container formatting objects

class Title(visualContainer):
    show: Any | None = None
    text: Any | None = None
    heading: Any | None = None
    titleWrap: Any | None = None
    fontColor: Any | None = None
    background: Any | None = None
    alignment: Any | None = None
    fontSize: Any | None = None
    bold: Any | None = None
    italic: Any | None = None
    underline: Any | None = None
    fontFamily: Any | None = None

class Subtitle(visualContainer):
    show: Any | None = None
    text: Any | None = None
    heading: Any | None = None
    titleWrap: Any | None = None
    fontColor: Any | None = None
    alignment: Any | None = None
    fontSize: Any | None = None
    bold: Any | None = None
    italic: Any | None = None
    underline: Any | None = None
    fontFamily: Any | None = None

class Divider(visualContainer):
    ignorePadding: Any | None = None
    show: Any | None = None
    color: Any | None = None
    width: Any | None = None
    style: Any | None = None

class Spacing(visualContainer):
    customizeSpacing: Any | None = None
    verticalSpacing: Any | None = None
    spaceBelowTitle: Any | None = None
    spaceBelowSubTitle: Any | None = None
    spaceBelowTitleArea: Any | None = None

class Padding(visualContainer):
    top: Any | None = None
    bottom: Any | None = None
    left: Any | None = None
    right: Any | None = None

class Visualcontainergeneralformattingobjects(visualContainer):
    x: Any | None = None
    y: Any | None = None
    width: Any | None = None
    height: Any | None = None
    altText: Any | None = None
    allowBinnedLineSample: Any | None = None
    allowOverlappingPointsSample: Any | None = None
    keepLayerOrder: Any | None = None

class Border(visualContainer):
    show: Any | None = None
    color: Any | None = None
    radius: Any | None = None
    width: Any | None = None

class Dropshadow(visualContainer):
    show: Any | None = None
    preset: Any | None = None
    position: Any | None = None
    color: Any | None = None
    transparency: Any | None = None
    shadowSpread: Any | None = None
    shadowBlur: Any | None = None
    angle: Any | None = None
    shadowDistance: Any | None = None

class Visuallink(visualContainer):
    show: Any | None = None
    type: Any | None = None
    bookmark: Any | None = None
    disabledTooltip: Any | None = None
    drillthroughSection: Any | None = None
    enabledTooltip: Any | None = None
    qna: Any | None = None
    suppressDefaultTooltip: Any | None = None
    showDefaultTooltip: Any | None = None
    navigationSection: Any | None = None
    tooltip: Any | None = None
    tooltipPlaceholderText: Any | None = None
    webUrl: Any | None = None
    dataFunction: Any | None = None

class Visualtooltip(visualContainer):
    show: Any | None = None
    type: Any | None = None
    section: Any | None = None
    titleFontColor: Any | None = None
    valueFontColor: Any | None = None
    fontSize: Any | None = None
    bold: Any | None = None
    italic: Any | None = None
    underline: Any | None = None
    fontFamily: Any | None = None
    background: Any | None = None
    transparency: Any | None = None
    actionFontColor: Any | None = None
    themedTitleFontColor: Any | None = None
    themedBackground: Any | None = None
    themedValueFontColor: Any | None = None

class Stylepreset(visualContainer):
    name: Any | None = None

class Visualheader(visualContainer):
    show: Any | None = None
    background: Any | None = None
    border: Any | None = None
    transparency: Any | None = None
    foreground: Any | None = None
    showVisualInformationButton: Any | None = None
    showVisualWarningButton: Any | None = None
    showVisualErrorButton: Any | None = None
    showDrillRoleSelector: Any | None = None
    showDrillUpButton: Any | None = None
    showDrillToggleButton: Any | None = None
    showDrillDownLevelButton: Any | None = None
    showDrillDownExpandButton: Any | None = None
    showPinButton: Any | None = None
    showFilterRestatementButton: Any | None = None
    showFocusModeButton: Any | None = None
    showCopyVisualImageButton: Any | None = None
    showSeeDataLayoutToggleButton: Any | None = None
    showOptionsMenu: Any | None = None
    showCommentButton: Any | None = None
    showTooltipButton: Any | None = None
    showPersonalizeVisualButton: Any | None = None
    showSmartNarrativeButton: Any | None = None
    showSetAlertButton: Any | None = None
    showFollowVisualButton: Any | None = None

class Visualheadertooltip(visualContainer):
    type: Any | None = None
    section: Any | None = None
    text: Any | None = None
    titleFontColor: Any | None = None
    fontSize: Any | None = None
    fontFamily: Any | None = None
    bold: Any | None = None
    italic: Any | None = None
    underline: Any | None = None
    background: Any | None = None
    transparency: Any | None = None
    themedTitleFontColor: Any | None = None
    themedBackground: Any | None = None

class VisualcontainerformattingobjectsTitleItem(visualContainer):
    selector: Selector | None = None
    properties: Title | None = None

class VisualcontainerformattingobjectsSubtitleItem(visualContainer):
    selector: Selector | None = None
    properties: Subtitle | None = None

class VisualcontainerformattingobjectsDividerItem(visualContainer):
    selector: Selector | None = None
    properties: Divider | None = None

class VisualcontainerformattingobjectsSpacingItem(visualContainer):
    selector: Selector | None = None
    properties: Spacing | None = None

class VisualcontainerformattingobjectsBackgroundItem(visualContainer):
    selector: Selector | None = None
    properties: Background | None = None

class VisualcontainerformattingobjectsPaddingItem(visualContainer):
    selector: Selector | None = None
    properties: Padding | None = None

class VisualcontainerformattingobjectsLockaspectItem(visualContainer):
    selector: Selector | None = None
    properties: Lockaspect | None = None

class VisualcontainerformattingobjectsGeneralItem(visualContainer):
    selector: Selector | None = None
    properties: Visualcontainergeneralformattingobjects | None = None

class VisualcontainerformattingobjectsBorderItem(visualContainer):
    selector: Selector | None = None
    properties: Border | None = None

class VisualcontainerformattingobjectsDropshadowItem(visualContainer):
    selector: Selector | None = None
    properties: Dropshadow | None = None

class VisualcontainerformattingobjectsVisuallinkItem(visualContainer):
    selector: Selector | None = None
    properties: Visuallink | None = None

class VisualcontainerformattingobjectsVisualtooltipItem(visualContainer):
    selector: Selector | None = None
    properties: Visualtooltip | None = None

class VisualcontainerformattingobjectsStylepresetItem(visualContainer):
    selector: Selector | None = None
    properties: Stylepreset | None = None

class VisualcontainerformattingobjectsVisualheaderItem(visualContainer):
    selector: Selector | None = None
    properties: Visualheader | None = None

class VisualcontainerformattingobjectsVisualheadertooltipItem(visualContainer):
    selector: Selector | None = None
    properties: Visualheadertooltip | None = None

class Visualcontainerformattingobjects(visualContainer):
    title: list[dict[str, Any]] | None = None
    subTitle: list[dict[str, Any]] | None = None
    divider: list[dict[str, Any]] | None = None
    spacing: list[dict[str, Any]] | None = None
    background: list[dict[str, Any]] | None = None
    padding: list[dict[str, Any]] | None = None
    lockAspect: list[dict[str, Any]] | None = None
    general: list[dict[str, Any]] | None = None
    border: list[dict[str, Any]] | None = None
    dropShadow: list[dict[str, Any]] | None = None
    visualLink: list[dict[str, Any]] | None = None
    visualTooltip: list[dict[str, Any]] | None = None
    stylePreset: list[dict[str, Any]] | None = None
    visualHeader: list[dict[str, Any]] | None = None
    visualHeaderTooltip: list[dict[str, Any]] | None = None

# Root visual class

class RootVisual(visualContainer):
    visualType: str | None = None
    autoSelectVisualType: bool | None = None
    query: Query | None = None
    expansionStates: list[Expansionstate] | None = None
    objects: Dataviewobjectdefinitions | None = None
    visualContainerObjects: Visualcontainerformattingobjects | None = None
    syncGroup: Visualsyncgroup | None = None
    drillFilterOtherVisuals: bool | None = None

# Filter configuration classes

class Filterdefinition(visualContainer):
    Version: float | None = None
    From: list[Entitysource] | None = None
    Where: list[Queryfilter] | None = None

class Filtercontainerformattingobjectsproperties(visualContainer):
    requireSingleSelect: Any | None = None
    isInvertedSelectionMode: Any | None = None

class FiltercontainerObjectsGeneralItem(visualContainer):
    selector: Selector | None = None
    properties: Filtercontainerformattingobjectsproperties | None = None

class Filtercontainerformattingobjects(visualContainer):
    general: list[dict[str, Any]] | None = None

class Filtercontainer(visualContainer):
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

class RootFilterconfig(visualContainer):
    filters: list[Filtercontainer] | None = None
    filterSortOrder: str | None = None
