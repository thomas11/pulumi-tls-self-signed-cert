# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._enums import *
import pulumi_tls

__all__ = ['SelfSignedCertificateArgs', 'SelfSignedCertificate']

@pulumi.input_type
class SelfSignedCertificateArgs:
    def __init__(__self__, *,
                 local_validity_period_hours: pulumi.Input[int],
                 subject: pulumi.Input['pulumi_tls.SelfSignedCertSubjectArgs'],
                 validity_period_hours: pulumi.Input[int],
                 algorithm: Optional[pulumi.Input['Algorithm']] = None,
                 allowed_uses: Optional[pulumi.Input[Sequence[pulumi.Input['AllowedUses']]]] = None,
                 dns_name: Optional[pulumi.Input[str]] = None,
                 ecdsa_curve: Optional[pulumi.Input['EcdsaCurve']] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 rsa_bits: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SelfSignedCertificate resource.
        :param pulumi.Input[int] local_validity_period_hours: Number of hours, after initial issuing, that the local certificate will remain valid for.
        :param pulumi.Input['pulumi_tls.SelfSignedCertSubjectArgs'] subject: The subject for which a certificate is being requested. The acceptable arguments are all optional and their naming is based upon [Issuer Distinguished Names (RFC5280)](https://tools.ietf.org/html/rfc5280#section-4.1.2.4) section.
        :param pulumi.Input[int] validity_period_hours: Number of hours, after initial issuing, that the certificate will remain valid for.
        :param pulumi.Input['Algorithm'] algorithm: Name of the algorithm to use when generating the private key. Currently-supported values are `RSA`, `ECDSA` and `ED25519` (default: `RSA`).
        :param pulumi.Input[Sequence[pulumi.Input['AllowedUses']]] allowed_uses: List of key usages allowed for the issued certificate. Values are defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) and combine flags defined by both [Key Usages](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3) and [Extended Key Usages](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12). Accepted values: `any_extended`, `cert_signing`, `client_auth`, `code_signing`, `content_commitment`, `crl_signing`, `data_encipherment`, `decipher_only`, `digital_signature`, `email_protection`, `encipher_only`, `ipsec_end_system`, `ipsec_tunnel`, `ipsec_user`, `key_agreement`, `key_encipherment`, `microsoft_commercial_code_signing`, `microsoft_kernel_code_signing`, `microsoft_server_gated_crypto`, `netscape_server_gated_crypto`, `ocsp_signing`, `server_auth`, `timestamping`.
        :param pulumi.Input[str] dns_name: The DNS name for which a certificate is being requested (i.e. certificate subjects).
        :param pulumi.Input['EcdsaCurve'] ecdsa_curve: When `algorithm` is `ECDSA`, the name of the elliptic curve to use. Currently-supported values are `P224`, `P256`, `P384` or `P521` (default: `P224`).
        :param pulumi.Input[str] ip_address: The IP address for which a certificate is being requested (i.e. certificate subjects).
        :param pulumi.Input[int] rsa_bits: When `algorithm` is `RSA`, the size of the generated RSA key, in bits (default: `2048`).
        """
        pulumi.set(__self__, "local_validity_period_hours", local_validity_period_hours)
        pulumi.set(__self__, "subject", subject)
        pulumi.set(__self__, "validity_period_hours", validity_period_hours)
        if algorithm is not None:
            pulumi.set(__self__, "algorithm", algorithm)
        if allowed_uses is not None:
            pulumi.set(__self__, "allowed_uses", allowed_uses)
        if dns_name is not None:
            pulumi.set(__self__, "dns_name", dns_name)
        if ecdsa_curve is not None:
            pulumi.set(__self__, "ecdsa_curve", ecdsa_curve)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if rsa_bits is not None:
            pulumi.set(__self__, "rsa_bits", rsa_bits)

    @property
    @pulumi.getter(name="localValidityPeriodHours")
    def local_validity_period_hours(self) -> pulumi.Input[int]:
        """
        Number of hours, after initial issuing, that the local certificate will remain valid for.
        """
        return pulumi.get(self, "local_validity_period_hours")

    @local_validity_period_hours.setter
    def local_validity_period_hours(self, value: pulumi.Input[int]):
        pulumi.set(self, "local_validity_period_hours", value)

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Input['pulumi_tls.SelfSignedCertSubjectArgs']:
        """
        The subject for which a certificate is being requested. The acceptable arguments are all optional and their naming is based upon [Issuer Distinguished Names (RFC5280)](https://tools.ietf.org/html/rfc5280#section-4.1.2.4) section.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: pulumi.Input['pulumi_tls.SelfSignedCertSubjectArgs']):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="validityPeriodHours")
    def validity_period_hours(self) -> pulumi.Input[int]:
        """
        Number of hours, after initial issuing, that the certificate will remain valid for.
        """
        return pulumi.get(self, "validity_period_hours")

    @validity_period_hours.setter
    def validity_period_hours(self, value: pulumi.Input[int]):
        pulumi.set(self, "validity_period_hours", value)

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input['Algorithm']]:
        """
        Name of the algorithm to use when generating the private key. Currently-supported values are `RSA`, `ECDSA` and `ED25519` (default: `RSA`).
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input['Algorithm']]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter(name="allowedUses")
    def allowed_uses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AllowedUses']]]]:
        """
        List of key usages allowed for the issued certificate. Values are defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) and combine flags defined by both [Key Usages](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3) and [Extended Key Usages](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12). Accepted values: `any_extended`, `cert_signing`, `client_auth`, `code_signing`, `content_commitment`, `crl_signing`, `data_encipherment`, `decipher_only`, `digital_signature`, `email_protection`, `encipher_only`, `ipsec_end_system`, `ipsec_tunnel`, `ipsec_user`, `key_agreement`, `key_encipherment`, `microsoft_commercial_code_signing`, `microsoft_kernel_code_signing`, `microsoft_server_gated_crypto`, `netscape_server_gated_crypto`, `ocsp_signing`, `server_auth`, `timestamping`.
        """
        return pulumi.get(self, "allowed_uses")

    @allowed_uses.setter
    def allowed_uses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AllowedUses']]]]):
        pulumi.set(self, "allowed_uses", value)

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS name for which a certificate is being requested (i.e. certificate subjects).
        """
        return pulumi.get(self, "dns_name")

    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_name", value)

    @property
    @pulumi.getter(name="ecdsaCurve")
    def ecdsa_curve(self) -> Optional[pulumi.Input['EcdsaCurve']]:
        """
        When `algorithm` is `ECDSA`, the name of the elliptic curve to use. Currently-supported values are `P224`, `P256`, `P384` or `P521` (default: `P224`).
        """
        return pulumi.get(self, "ecdsa_curve")

    @ecdsa_curve.setter
    def ecdsa_curve(self, value: Optional[pulumi.Input['EcdsaCurve']]):
        pulumi.set(self, "ecdsa_curve", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address for which a certificate is being requested (i.e. certificate subjects).
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="rsaBits")
    def rsa_bits(self) -> Optional[pulumi.Input[int]]:
        """
        When `algorithm` is `RSA`, the size of the generated RSA key, in bits (default: `2048`).
        """
        return pulumi.get(self, "rsa_bits")

    @rsa_bits.setter
    def rsa_bits(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rsa_bits", value)


class SelfSignedCertificate(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input['Algorithm']] = None,
                 allowed_uses: Optional[pulumi.Input[Sequence[pulumi.Input['AllowedUses']]]] = None,
                 dns_name: Optional[pulumi.Input[str]] = None,
                 ecdsa_curve: Optional[pulumi.Input['EcdsaCurve']] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 local_validity_period_hours: Optional[pulumi.Input[int]] = None,
                 rsa_bits: Optional[pulumi.Input[int]] = None,
                 subject: Optional[pulumi.Input[pulumi.InputType['pulumi_tls.SelfSignedCertSubjectArgs']]] = None,
                 validity_period_hours: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a SelfSignedCertificate resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['Algorithm'] algorithm: Name of the algorithm to use when generating the private key. Currently-supported values are `RSA`, `ECDSA` and `ED25519` (default: `RSA`).
        :param pulumi.Input[Sequence[pulumi.Input['AllowedUses']]] allowed_uses: List of key usages allowed for the issued certificate. Values are defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) and combine flags defined by both [Key Usages](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3) and [Extended Key Usages](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12). Accepted values: `any_extended`, `cert_signing`, `client_auth`, `code_signing`, `content_commitment`, `crl_signing`, `data_encipherment`, `decipher_only`, `digital_signature`, `email_protection`, `encipher_only`, `ipsec_end_system`, `ipsec_tunnel`, `ipsec_user`, `key_agreement`, `key_encipherment`, `microsoft_commercial_code_signing`, `microsoft_kernel_code_signing`, `microsoft_server_gated_crypto`, `netscape_server_gated_crypto`, `ocsp_signing`, `server_auth`, `timestamping`.
        :param pulumi.Input[str] dns_name: The DNS name for which a certificate is being requested (i.e. certificate subjects).
        :param pulumi.Input['EcdsaCurve'] ecdsa_curve: When `algorithm` is `ECDSA`, the name of the elliptic curve to use. Currently-supported values are `P224`, `P256`, `P384` or `P521` (default: `P224`).
        :param pulumi.Input[str] ip_address: The IP address for which a certificate is being requested (i.e. certificate subjects).
        :param pulumi.Input[int] local_validity_period_hours: Number of hours, after initial issuing, that the local certificate will remain valid for.
        :param pulumi.Input[int] rsa_bits: When `algorithm` is `RSA`, the size of the generated RSA key, in bits (default: `2048`).
        :param pulumi.Input[pulumi.InputType['pulumi_tls.SelfSignedCertSubjectArgs']] subject: The subject for which a certificate is being requested. The acceptable arguments are all optional and their naming is based upon [Issuer Distinguished Names (RFC5280)](https://tools.ietf.org/html/rfc5280#section-4.1.2.4) section.
        :param pulumi.Input[int] validity_period_hours: Number of hours, after initial issuing, that the certificate will remain valid for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SelfSignedCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SelfSignedCertificate resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SelfSignedCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SelfSignedCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input['Algorithm']] = None,
                 allowed_uses: Optional[pulumi.Input[Sequence[pulumi.Input['AllowedUses']]]] = None,
                 dns_name: Optional[pulumi.Input[str]] = None,
                 ecdsa_curve: Optional[pulumi.Input['EcdsaCurve']] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 local_validity_period_hours: Optional[pulumi.Input[int]] = None,
                 rsa_bits: Optional[pulumi.Input[int]] = None,
                 subject: Optional[pulumi.Input[pulumi.InputType['pulumi_tls.SelfSignedCertSubjectArgs']]] = None,
                 validity_period_hours: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SelfSignedCertificateArgs.__new__(SelfSignedCertificateArgs)

            __props__.__dict__["algorithm"] = algorithm
            __props__.__dict__["allowed_uses"] = allowed_uses
            __props__.__dict__["dns_name"] = dns_name
            __props__.__dict__["ecdsa_curve"] = ecdsa_curve
            __props__.__dict__["ip_address"] = ip_address
            if local_validity_period_hours is None and not opts.urn:
                raise TypeError("Missing required property 'local_validity_period_hours'")
            __props__.__dict__["local_validity_period_hours"] = local_validity_period_hours
            __props__.__dict__["rsa_bits"] = rsa_bits
            if subject is None and not opts.urn:
                raise TypeError("Missing required property 'subject'")
            __props__.__dict__["subject"] = subject
            if validity_period_hours is None and not opts.urn:
                raise TypeError("Missing required property 'validity_period_hours'")
            __props__.__dict__["validity_period_hours"] = validity_period_hours
            __props__.__dict__["ca_cert"] = None
            __props__.__dict__["pem"] = None
            __props__.__dict__["private_key"] = None
        super(SelfSignedCertificate, __self__).__init__(
            'tls-self-signed-cert:index:SelfSignedCertificate',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter
    def pem(self) -> pulumi.Output[str]:
        return pulumi.get(self, "pem")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_key")

