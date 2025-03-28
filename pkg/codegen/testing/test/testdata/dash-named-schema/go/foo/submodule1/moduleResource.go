// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package submodule1

import (
	"context"
	"reflect"

	"dash-named-schema/foo"
	"dash-named-schema/foo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type ModuleResource struct {
	pulumi.CustomResourceState

	Thing foo.TopLevelPtrOutput `pulumi:"thing"`
}

// NewModuleResource registers a new resource with the given unique name, arguments, and options.
func NewModuleResource(ctx *pulumi.Context,
	name string, args *ModuleResourceArgs, opts ...pulumi.ResourceOption) (*ModuleResource, error) {
	if args == nil {
		args = &ModuleResourceArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ModuleResource
	err := ctx.RegisterResource("foo-bar:submodule1:ModuleResource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModuleResource gets an existing ModuleResource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModuleResource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModuleResourceState, opts ...pulumi.ResourceOption) (*ModuleResource, error) {
	var resource ModuleResource
	err := ctx.ReadResource("foo-bar:submodule1:ModuleResource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ModuleResource resources.
type moduleResourceState struct {
}

type ModuleResourceState struct {
}

func (ModuleResourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*moduleResourceState)(nil)).Elem()
}

type moduleResourceArgs struct {
	Thing *foo.TopLevel `pulumi:"thing"`
}

// The set of arguments for constructing a ModuleResource resource.
type ModuleResourceArgs struct {
	Thing foo.TopLevelPtrInput
}

func (ModuleResourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*moduleResourceArgs)(nil)).Elem()
}

type ModuleResourceInput interface {
	pulumi.Input

	ToModuleResourceOutput() ModuleResourceOutput
	ToModuleResourceOutputWithContext(ctx context.Context) ModuleResourceOutput
}

func (*ModuleResource) ElementType() reflect.Type {
	return reflect.TypeOf((**ModuleResource)(nil)).Elem()
}

func (i *ModuleResource) ToModuleResourceOutput() ModuleResourceOutput {
	return i.ToModuleResourceOutputWithContext(context.Background())
}

func (i *ModuleResource) ToModuleResourceOutputWithContext(ctx context.Context) ModuleResourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModuleResourceOutput)
}

func (i *ModuleResource) ToOutput(ctx context.Context) pulumix.Output[*ModuleResource] {
	return pulumix.Output[*ModuleResource]{
		OutputState: i.ToModuleResourceOutputWithContext(ctx).OutputState,
	}
}

type ModuleResourceOutput struct{ *pulumi.OutputState }

func (ModuleResourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ModuleResource)(nil)).Elem()
}

func (o ModuleResourceOutput) ToModuleResourceOutput() ModuleResourceOutput {
	return o
}

func (o ModuleResourceOutput) ToModuleResourceOutputWithContext(ctx context.Context) ModuleResourceOutput {
	return o
}

func (o ModuleResourceOutput) ToOutput(ctx context.Context) pulumix.Output[*ModuleResource] {
	return pulumix.Output[*ModuleResource]{
		OutputState: o.OutputState,
	}
}

func (o ModuleResourceOutput) Thing() foo.TopLevelPtrOutput {
	return o.ApplyT(func(v *ModuleResource) foo.TopLevelPtrOutput { return v.Thing }).(foo.TopLevelPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ModuleResourceInput)(nil)).Elem(), &ModuleResource{})
	pulumi.RegisterOutputType(ModuleResourceOutput{})
}
