// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package example

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"simple-resource-schema-custom-pypackage-name/example/internal"
)

func ArgFunction(ctx *pulumi.Context, args *ArgFunctionArgs, opts ...pulumi.InvokeOption) (*ArgFunctionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv ArgFunctionResult
	err := ctx.Invoke("example::argFunction", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type ArgFunctionArgs struct {
	Arg1 *Resource `pulumi:"arg1"`
}

type ArgFunctionResult struct {
	Result *Resource `pulumi:"result"`
}

func ArgFunctionOutput(ctx *pulumi.Context, args ArgFunctionOutputArgs, opts ...pulumi.InvokeOption) ArgFunctionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ArgFunctionResult, error) {
			args := v.(ArgFunctionArgs)
			r, err := ArgFunction(ctx, &args, opts...)
			var s ArgFunctionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(ArgFunctionResultOutput)
}

type ArgFunctionOutputArgs struct {
	Arg1 ResourceInput `pulumi:"arg1"`
}

func (ArgFunctionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ArgFunctionArgs)(nil)).Elem()
}

type ArgFunctionResultOutput struct{ *pulumi.OutputState }

func (ArgFunctionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ArgFunctionResult)(nil)).Elem()
}

func (o ArgFunctionResultOutput) ToArgFunctionResultOutput() ArgFunctionResultOutput {
	return o
}

func (o ArgFunctionResultOutput) ToArgFunctionResultOutputWithContext(ctx context.Context) ArgFunctionResultOutput {
	return o
}

func (o ArgFunctionResultOutput) ToOutput(ctx context.Context) pulumix.Output[ArgFunctionResult] {
	return pulumix.Output[ArgFunctionResult]{
		OutputState: o.OutputState,
	}
}

func (o ArgFunctionResultOutput) Result() ResourceOutput {
	return o.ApplyT(func(v ArgFunctionResult) *Resource { return v.Result }).(ResourceOutput)
}

func init() {
	pulumi.RegisterOutputType(ArgFunctionResultOutput{})
}
