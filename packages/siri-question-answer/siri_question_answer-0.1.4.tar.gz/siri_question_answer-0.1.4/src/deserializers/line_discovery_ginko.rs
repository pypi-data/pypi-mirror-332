use quick_xml::de::from_str;
use serde::Deserialize;

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "Envelope")]
pub struct Envelope {
    #[serde(rename = "Header")]
    pub header: String, 
    #[serde(rename = "Body")]
    pub body: Body,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "Body")]
pub struct Body {
    #[serde(rename = "LinesDiscoveryResponse")]
    pub lines_discovery_response: LinesDiscoveryResponse,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "LinesDiscoveryResponse")]
pub struct LinesDiscoveryResponse {
    #[serde(rename = "ServiceDeliveryInfo")]
    pub service_delivery_info: ServiceDeliveryInfo,
    #[serde(rename = "Answer")]
    pub answer: Answer,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "ServiceDeliveryInfo")]
pub struct ServiceDeliveryInfo {
    #[serde(rename = "ResponseTimestamp")]
    pub response_timestamp: String,
    #[serde(rename = "ProducerRef")]
    pub producer_ref: String,
    #[serde(rename = "ResponseMessageIdentifier")]
    pub response_message_identifier: String,
    #[serde(rename = "RequestMessageRef")]
    pub request_message_ref: String,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "Answer")]
pub struct Answer {
    #[serde(rename = "ResponseTimestamp")]
    pub response_timestamp: String,
    #[serde(rename = "AnnotatedLineRef")]
    pub annotated_line_refs: Vec<AnnotatedLineRef>,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "AnnotatedLineRef")]
pub struct AnnotatedLineRef {
    #[serde(rename = "LineRef")]
    pub line_ref: String,
    #[serde(rename = "LineName")]
    pub line_name: String,
    #[serde(rename = "Monitored")]
    pub monitored: bool,
    #[serde(rename = "Destinations")]
    pub destinations: Destinations,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "Destinations")]
pub struct Destinations {
    #[serde(rename = "Destination")]
    pub destination: Vec<Destination>,
}

#[derive(Debug, Deserialize, PartialEq, Clone)]
#[serde(rename_all = "PascalCase", rename = "Destination")]
pub struct Destination {
    #[serde(rename = "DestinationRef")]
    pub destination_ref: String,
    #[serde(rename = "DirectionRef")]
    pub direction_ref: String,
}

/// Deserialize a LinesDiscoveryResponse from XML.
/// 
/// # Parameters
/// 
/// - `xml` - The XML to deserialize.
pub fn deserialize_lines_discovery_response(xml: &str) -> Result<Envelope, quick_xml::DeError> {
    from_str(xml)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_deserialize_lines_discovery_response() {
        let xml = r#"
            <Envelope xmlns="http://www.w3.org/2003/05/soap-envelope" xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <soap:Header></soap:Header>
                <Body>
                    <LinesDiscoveryResponse>
                        <ServiceDeliveryInfo>
                            <ResponseTimestamp>2021-08-31T14:00:00Z</ResponseTimestamp>
                            <ProducerRef>ProducerRef</ProducerRef>
                            <ResponseMessageIdentifier>ResponseMessageIdentifier</ResponseMessageIdentifier>
                            <RequestMessageRef>RequestMessageRef</RequestMessageRef>
                        </ServiceDeliveryInfo>
                        <Answer>
                            <ResponseTimestamp>2021-08-31T14:00:00Z</ResponseTimestamp>
                            <AnnotatedLineRef>
                                <LineRef>421</LineRef>
                                <LineName>D421</LineName>
                                <Monitored>true</Monitored>
                                <Destinations>
                                    <Destination>
                                    <DestinationRef>COLLUM1</DestinationRef>
                                    <DirectionRef>Aller</DirectionRef>
                                    </Destination>
                                    <Destination>
                                    <DestinationRef>ARGUEL02</DestinationRef>
                                    <DirectionRef>Retour</DirectionRef>
                                    </Destination>
                                </Destinations>
                            </AnnotatedLineRef>
                            <version>version</version>
                        </Answer>
                    </LinesDiscoveryResponse>
                </Body>
            </Envelope>
        "#;

        let expected = Envelope {
            header: "".to_string(),
            body: Body {
                lines_discovery_response: LinesDiscoveryResponse {
                    service_delivery_info: ServiceDeliveryInfo {
                        response_timestamp: "2021-08-31T14:00:00Z".to_string(),
                        producer_ref: "ProducerRef".to_string(),
                        response_message_identifier: "ResponseMessageIdentifier".to_string(),
                        request_message_ref: "RequestMessageRef".to_string(),
                    },
                    answer: Answer {
                        response_timestamp: "2021-08-31T14:00:00Z".to_string(),
                        annotated_line_refs: vec![
                            AnnotatedLineRef {
                                line_ref: "421".to_string(),
                                line_name: "D421".to_string(),
                                monitored: true,
                                destinations: Destinations {
                                    destination: vec![
                                        Destination {
                                            destination_ref: "COLLUM1".to_string(),
                                            direction_ref: "Aller".to_string(),
                                        },
                                        Destination {
                                            destination_ref: "ARGUEL02".to_string(),
                                            direction_ref: "Retour".to_string(),
                                        },
                                    ],
                                },
                            },
                        ],
                    },
                },
            }
        };

        let result: Envelope = from_str(xml).unwrap();
        assert_eq!(result, expected);
    }
}
